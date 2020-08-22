import json 

from common.test_case import UdPlatformsTestCase
from django.urls import reverse

from ..tests import AddressFactory
from users.models import Address
from rest_framework import status

class AddressListApiTest(UdPlatformsTestCase):
    # ================================
    # Basic setup  
    # ================================
    url = reverse('address-list')

    def setUp(self):
        super(UdPlatformsTestCase, self).setUp()

    def test_address_list_get(self):
        # ===========================================
        # Check address List get successfully or not 
        # ===========================================
        _ = AddressFactory.create_batch(4)

        request = self.client.get(self.url)

        self.assertSuccess(request)
        self.assertEqual(len(request.data), 4)


    def test_address_list_post(self):
        # ===========================================
        # Check address data saved successfully or not 
        # ===========================================
        data = {
            'street': 'Road no 78',
            'city': 'Dhaka',
            'state': 'Sukrabad',
            'zip_code':'1207'
        }

        request = self.client.post(self.url, data)
        self.assertCreated(request)

        self.assertEqual(Address.objects.count(), 1)
        self.assertEqual(request.data['state'], data['state'])
        self.assertEqual(request.data['city'], data['city'])
        self.assertEqual(request.data['street'], data['street'])
        self.assertEqual(request.data['zip_code'], data['zip_code'])


class AddressDetailsApiTest(UdPlatformsTestCase):
    # ================================
    # Basic setup  
    # ================================
    def setUp(self):
        super(UdPlatformsTestCase, self).setUp()

        # Set an address
        self.address = AddressFactory()
        
        #set the url
        self.url = reverse('address-detail', args=[self.address.alias])

    def test_address_details_get(self):
        # ================================
        # Check address get Sucessfully or not  
        # ================================
        request = self.client.get(self.url)

        self.assertSuccess(request)
        self.assertEqual(request.data['id'], self.address.id)

    def test_address_details_put(self):
        # ================================
        # Check address update  
        # ================================
        data = {
            'street': 'Road 90',
            'city': 'Dhaka',
            'state': 'BD',
            'zip_code':'1800'
        }

        request = self.client.put(self.url, data=json.dumps(dict(data)),
                                    content_type='application/json')

        self.assertSuccess(request)
        self.assertEqual(request.data['state'], data['state'])
        self.assertEqual(request.data['city'], data['city'])
        self.assertEqual(request.data['street'], data['street'])
        self.assertEqual(request.data['zip_code'], data['zip_code'])

    def test_address_details_delete(self):
        # ================================
        # Check address delete  
        # ================================
        request = self.client.get(self.url)
        self.assertEqual(Address.objects.count(), 1)

        request = self.client.delete(self.url)
        self.assertTrue(status.is_success(request.status_code))

        request = self.client.delete(self.url)
        self.assertFalse(status.is_success(request.status_code))
