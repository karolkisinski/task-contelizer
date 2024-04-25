import io
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from unittest.mock import patch


class TextRandomTests(APITestCase):
    @patch('text_random.views.RandomizeText.process_file')
    def test_successful_file_upload(self, mock_process_file):
        mock_process_file.return_value = 'Mocked processed text'

        file_content = b'Test file content.'
        file_object = io.BytesIO(file_content)
        file_object.name = 'test_file.txt'

        url = reverse('process-text')
        data = {'file': file_object}
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['processed_text'], 'Mocked processed text')

    def test_invalid_file_upload(self):
        url = reverse('process-text')
        data = {}
        response = self.client.post(url, data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('file', response.data)
