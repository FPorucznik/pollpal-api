from rest_framework import generics
from .serializers import PollSerializer, VoteSerializer
from .models import Poll, Vote


class PollListView(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class CreatePollView(generics.CreateAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()


class CreateVoteView(generics.CreateAPIView):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()


class PollGetView(generics.RetrieveAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
