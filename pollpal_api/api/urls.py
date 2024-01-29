from django.urls import path
from .views import CreatePollView, PollListView

urlpatterns = [
    path('polls/', PollListView.as_view(), name='polls_list'),
    path('polls/create/', CreatePollView.as_view(), name='poll_create'),
]
