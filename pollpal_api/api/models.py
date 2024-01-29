from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_active = models.BooleanField()

class Option(models.Model):
    text = models.CharField(max_length=150)
    poll = models.ForeignKey(Poll, related_name='options', on_delete=models.CASCADE)

class Vote(models.Model):
    option = models.ForeignKey(Option, related_name='votes', on_delete=models.CASCADE)
    user_ip = models.GenericIPAddressField()