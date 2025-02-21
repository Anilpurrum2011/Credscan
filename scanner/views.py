from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from .forms import DocumentForm
from .models import Document
import difflib

def home(request):
    return render(request, 'scanner/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a UserProfile for the new user
            UserProfile.objects.create(user=user)
            # Log the user in
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'scanner/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'scanner/login.html', {'error': 'Invalid credentials'})
    return render(request, 'scanner/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # If UserProfile doesn't exist, create it
        user_profile = UserProfile.objects.create(user=request.user)
    return render(request, 'scanner/profile.html', {'profile': user_profile})

from django.shortcuts import render, redirect
from .models import CreditRequest

def request_credits(request):
    if request.method == 'POST':
        requested_credits = int(request.POST['credits'])
        CreditRequest.objects.create(user=request.user, requested_credits=requested_credits)
        return redirect('profile')
    return render(request, 'scanner/request_credits.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import CreditRequest, UserProfile

# Check if the user is an admin
def is_admin(user):
    return user.is_staff

# Admin dashboard to view pending credit requests
@user_passes_test(is_admin)
def admin_dashboard(request):
    print("Admin dashboard view called")  # Debugging
    credit_requests = CreditRequest.objects.filter(approved=False)
    return render(request, 'scanner/admin_dashboard.html', {'credit_requests': credit_requests})

# View to approve credit requests
@user_passes_test(is_admin)
def approve_credits(request, request_id):
    credit_request = get_object_or_404(CreditRequest, id=request_id)
    credit_request.approved = True
    credit_request.save()

    # Add the requested credits to the user's profile
    user_profile = UserProfile.objects.get(user=credit_request.user)
    user_profile.credits += credit_request.requested_credits
    user_profile.save()

    return redirect('admin_dashboard')

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import CreditRequest

# Check if the user is an admin
def is_admin(user):
    return user.is_staff

# Admin dashboard to view pending credit requests
@user_passes_test(is_admin)
def admin_dashboard(request):
    credit_requests = CreditRequest.objects.filter(approved=False)
    return render(request, 'scanner/admin_dashboard.html', {'credit_requests': credit_requests})

@login_required
def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.user = request.user
            document.save()

            # Deduct 1 credit for the scan
            user_profile = request.user.userprofile
            user_profile.credits -= 1
            user_profile.save()

            return redirect('matches', docId=document.id)
    else:
        form = DocumentForm()
    return render(request, 'scanner/upload.html', {'form': form})

@login_required
def find_matches(request, docId):
    try:
        # Get the uploaded document
        uploaded_document = Document.objects.get(id=docId)
        all_documents = Document.objects.exclude(id=docId)

        # Read the content of the uploaded document
        uploaded_content = uploaded_document.file.read().decode('utf-8')

        matches = []
        for doc in all_documents:
            # Read the content of each stored document
            doc.file.open('r')  # Open the file in read mode
            doc_content = doc.file.read().decode('utf-8')
            doc.file.close()  # Close the file after reading

            # Calculate similarity using difflib
            similarity = difflib.SequenceMatcher(None, uploaded_content, doc_content).ratio()

            # Add to matches if similarity is above a threshold (e.g., 0.7)
            if similarity > 0.7:
                matches.append((doc, similarity))

        return render(request, 'scanner/matches.html', {'matches': matches})
    except Exception as e:
        print(f"Error in find_matches: {e}")
        return render(request, 'scanner/matches.html', {'matches': []})