from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_active = models.BooleanField()
