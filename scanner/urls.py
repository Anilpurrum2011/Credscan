from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('request_credits/', views.request_credits, name='request_credits'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/approve_credits/<int:request_id>/', views.approve_credits, name='approve_credits'),
    path('upload/', views.upload_document, name='upload'),  # Document upload
    path('matches/<int:docId>/', views.find_matches, name='matches'),  # Matching documents
]