from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Option, Poll, Vote
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from django.urls import reverse

class PollsTest(APITestCase):
    def setUp(self):
        self.current_date = datetime.now()
        self.expires_at_date = make_aware(self.current_date + timedelta(days=1))

    def test_polls_get_list(self):
        Poll.objects.create(
            question='Test question ?',
            created_at=self.current_date,
            expires_at=self.expires_at_date,
            is_active=True
        )
        Poll.objects.create(
            question='Another test question ?',
            created_at=self.current_date,
            expires_at=self.expires_at_date,
            is_active=True
        )
        url = reverse('polls_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
    
    def test_polls_create(self):
        url = reverse('poll_create')

        options = [
            {'text': 'option 1'},
            {'text': 'option 2'}
        ]
        data = {
            'question': 'Test question ?',
            'expires_at': self.expires_at_date,
            'is_active': True,
            'options': options
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Poll.objects.all().count(), 1)
        self.assertEqual(Option.objects.all().count(), 2)