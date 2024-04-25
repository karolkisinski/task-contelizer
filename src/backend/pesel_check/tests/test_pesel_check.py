from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from unittest.mock import patch


class PeselValidationViewTests(APITestCase):
    @patch('pesel_check.views.Pesel.validate')
    @patch('pesel_check.views.Pesel.get_gender')
    @patch('pesel_check.views.Pesel.get_birth_date')
    def test_valid_pesel(self, mock_get_birth_date, mock_get_gender,
                         mock_validate):
        mock_validate.return_value = True
        mock_get_gender.return_value = 'Male'
        mock_get_birth_date.return_value = '1990-01-01'

        url = reverse('validate_pesel')
        data = {'pesel': '12345678901'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['message'], 'Pesel jest prawidowy')
        self.assertEqual(response.data['gender'], 'Male')
        self.assertEqual(response.data['birth_date'], '1990-01-01')

    @patch('pesel_check.views.Pesel.validate')
    def test_invalid_pesel(self, mock_validate):
        mock_validate.return_value = False

        url = reverse('validate_pesel')
        data = {'pesel': '12345678900'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Pesel jest nieprawidowy')
