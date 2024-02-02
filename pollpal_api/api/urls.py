from django.urls import path
from .views import CreatePollView, PollListView, CreateVoteView, PollGetView

urlpatterns = [
    path('polls/', PollListView.as_view(), name='poll_list'),
    path('polls/<int:pk>/', PollGetView.as_view(), name='poll_get'),
    path('polls/create/', CreatePollView.as_view(), name='poll_create'),
    path('polls/vote/', CreateVoteView.as_view(), name='poll_vote'),
]
