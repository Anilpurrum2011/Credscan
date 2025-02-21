from django.utils import timezone
from .models import UserProfile

class CreditResetMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only reset credits for authenticated users
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                profile.reset_credits()
            except UserProfile.DoesNotExist:
                # If UserProfile doesn't exist, create it
                UserProfile.objects.create(user=request.user)
        response = self.get_response(request)
        return response