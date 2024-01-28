from django.contrib import admin
from .models import Option, Poll

admin.site.register([Option, Poll])