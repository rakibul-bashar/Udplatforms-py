from django.test import TestCase
from rest_framework.test import APIClient


class UdPlatformsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def assertCreated(self, request):
        self.assertEqual(request.status_code, 201)

    def assertSuccess(self, request):
        self.assertEqual(request.status_code, 200)

    def assertDeleted(self, request):
        self.assertEqual(request.status_code, 204)

    def assertBadRequest(self, request):
        self.assertEqual(request.status_code, 400)

    def assertPermissionDenied(self, request):
        self.assertEqual(request.status_code, 403)

    def assertNotFound(self, request):
        self.assertEqual(request.status_code, 404)

    def assertMethodNotAllowed(self, request):
        self.assertEqual(request.status_code, 405)