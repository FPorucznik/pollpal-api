from rest_framework import generics
from .serializers import PollSerializer
from .models import Poll

class PollListView(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer