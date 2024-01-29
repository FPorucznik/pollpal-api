from django.contrib import admin
from .models import Option, Poll, Vote

admin.site.register([Option, Poll, Vote])