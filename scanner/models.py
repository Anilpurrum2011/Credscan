from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credits = models.IntegerField(default=20)
    last_reset = models.DateTimeField(default=timezone.now)

    def reset_credits(self):
        # Reset credits to 20 if the last reset was more than 24 hours ago
        if (timezone.now() - self.last_reset).days >= 1:
            self.credits = 20
            self.last_reset = timezone.now()
            self.save()

    def __str__(self):
        return self.user.username

class CreditRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_credits = models.IntegerField()
    approved = models.BooleanField(default=False)
    requested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.requested_credits} credits"
    
from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name