from django.urls import path
from .views import PollListView

urlpatterns = [
    path('polls/', PollListView.as_view(), name='polls_list'),
]
