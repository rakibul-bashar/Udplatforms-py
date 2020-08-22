import random
import json

from common.test_case import UdPlatformsTestCase
from django.urls import reverse

from ..tests import UserFactory, AddressFactory
from users.models import User
from rest_framework import status


class UserListApiTest(UdPlatformsTestCase):
    # ================================
    # Basic setup  
    # ================================
    url = reverse('user-list')

    def setUp(self):
        super(UdPlatformsTestCase, self).setUp()
    
    def test_user_list_get(self):
        # ===========================================
        # Check User List get successfully or not 
        # ===========================================
        _ = UserFactory.create_batch(4)

        request = self.client.get(self.url)

        self.assertSuccess(request)
        self.assertEqual(len(request.data), 4)

    def test_user_list_post(self):
        # ===========================================
        # Check user data saved successfully or not 
        # ===========================================
        data = {
            'first_name': 'rakibul',
            'last_name': 'bashar',
            'addresses': AddressFactory().id,
            'user_type':random.choice(['PARENT', 'CHILD'])
        }
        if data['user_type'] == 'CHILD':
            data['addresses'] = ''

        self.url = reverse('create-user')

        request = self.client.post(self.url, data)

        self.assertCreated(request)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(request.data['first_name'], data['first_name'])
        self.assertEqual(request.data['last_name'], data['last_name'])
        self.assertEqual(request.data['user_type'], data['user_type'])
        if data['user_type'] == 'CHILD':
            self.assertEqual(request.data['addresses'], None)
        else:
            self.assertEqual(request.data['addresses'], data['addresses'])


    def test_user_details_get(self):
        # ================================
        # Check User get Sucessfully or not  
        # ================================
        user = UserFactory()
        self.url = reverse('user-details', args=[user.alias])
        request = self.client.get(self.url)
        self.assertSuccess(request)
        self.assertEqual(request.data['id'], user.id)

    def test_user_details_put(self):
        # ================================
        # Check User update  
        # ================================
        data = {
            'first_name': 'rakib',
            'last_name': 'bhai',
            'addresses': AddressFactory().id,
            'user_type':random.choice(['PARENT', 'CHILD'])
        }
        if data['user_type'] == 'CHILD':
            data['addresses'] = ''
        user = UserFactory()
        self.url = reverse('user-details', args=[user.alias])
        request = self.client.put(self.url, data=json.dumps(dict(data)),
                                content_type='application/json')
        self.assertSuccess(request)
        self.assertEqual(request.data['first_name'], data['first_name'])
        self.assertEqual(request.data['last_name'], data['last_name'])
        self.assertEqual(request.data['user_type'], data['user_type'])
        if data['user_type'] == 'CHILD':
            self.assertEqual(request.data['addresses'], None)
        else:
            self.assertEqual(request.data['addresses'], data['addresses'])

    def test_user_details_delete(self):
        # ================================
        # Check User delete  
        # ================================
        user = UserFactory()
        self.url = reverse('user-details', args=[user.alias])
        request = self.client.get(self.url)
        self.assertEqual(User.objects.count(), 1)

        request = self.client.delete(self.url)
        self.assertTrue(status.is_success(request.status_code))

        request = self.client.delete(self.url)
        self.assertFalse(status.is_success(request.status_code))