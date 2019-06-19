from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

client = APIClient()


class BikeRentalTests(APITestCase):
    """
    It's test cases of bike rentals api endpoints.
    """

    def test_get_check_url(self):
        """
        test the url endpoints.
        """
        response = client.get('/api/v1/bike-rentals/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_standard_deviation(self):
        """ test the success response of the bike rental api endpoints. """
        response = client.get('/api/v1/bike-rentals/')
        
        self.assertEqual(response.json()['message'], 'The standard deviation of week day.')
        self.assertEqual(response.json()['status'], status.HTTP_200_OK)
