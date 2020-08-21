from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status

from django.contrib.auth.models import User


class FoodAPITests(APITestCase):

    def setUp(self):
        test_user1 = User.objects.create(username='Guido_Rossum', password='python123')
        self.test_user1_token = 'Token ' + str(Token.objects.get_or_create(user=test_user1)[0])

        test_user2 = User.objects.create(username='Linus_Torvalds', password='linux123')
        self.test_user2_token = 'Token ' + str(Token.objects.get_or_create(user=test_user2)[0])

        self.restaurant_data = {
            'name': 'Ресторан на Арбате',
            'address': 'Москва, ул. Арбат',
            'works_from': '8:00:00',
            'works_until': '22:00:00',
            'img': None,
            'dishes': []
        }
        self.ingredient_data = {
            'name': 'Авокадо',
            'calories': 160
        }

    def test_create_without_token(self):
        """
        Test that user cannot create ingredient without Token
        """
        url = '/api/ingredients/'
        client = APIClient()

        response = client.post(url, self.ingredient_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_with_token(self):
        """
        Test that user can create ingredient with Token
        """
        url = '/api/ingredients/'
        client = APIClient()

        client.credentials(HTTP_AUTHORIZATION=self.test_user1_token)
        response = client.post(url, self.ingredient_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_restaurant_without_token(self):
        """
        Test that a user cannot create a restaurant without Token
        """
        url = '/api/places/'
        client = APIClient()

        response = client.post(url, self.restaurant_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_restaurant_with_token(self):
        """
        Test that a user can create a restaurant with Token
        """
        url = '/api/places/'
        client = APIClient()

        client.credentials(HTTP_AUTHORIZATION=self.test_user1_token)
        response = client.post(url, self.restaurant_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_retrieve_restaurant(self):
        """
        Test that a user can get info about some restaurant
        """
        response = self.client.get(f'/api/places/1/', format='json')
        self.assertNotEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_get_restaurants_list(self):
        """
        Test that a user can get list of restaurants
        """
        response = self.client.get('/api/places/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_request_by_owner(self):
        """
        Test that owner can send 'PUT' request to its restaurant
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=self.test_user1_token)
        response = client.post('/api/places/', self.restaurant_data, format='json')
        url = f"/api/places/{response.data['id']}/"

        response = client.put(url, self.restaurant_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_request_by_owner(self):
        """
        Test that owner can send 'PATCH' request to its restaurant
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=self.test_user2_token)
        response = client.post('/api/places/', self.restaurant_data, format='json')
        url = f"/api/places/{response.data['id']}/"

        response = client.patch(url, self.restaurant_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_request_by_owner(self):
        """
        Test that owner can send 'DELETE' request to its restaurant
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=self.test_user2_token)
        response = client.post('/api/places/', self.restaurant_data, format='json')
        url = f"/api/places/{response.data['id']}/"

        response = client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_request_by_non_owner(self):
        """
        Test that non owner cannot send 'PUT' request to some restaurant
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=self.test_user2_token)
        response = client.post('/api/places/', self.restaurant_data, format='json')
        url = f"/api/places/{response.data['id']}/"

        client.credentials(HTTP_AUTHORIZATION=self.test_user1_token)
        response = client.put(url, self.restaurant_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_request_by_non_owner(self):
        """
        Test that non owner cannot send 'PATCH' request to some restaurant
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=self.test_user2_token)
        response = client.post('/api/places/', self.restaurant_data, format='json')
        url = f"/api/places/{response.data['id']}/"

        client.credentials(HTTP_AUTHORIZATION=self.test_user1_token)
        response = client.patch(url, self.restaurant_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_request_by_non_owner(self):
        """
        Test that non owner cannot send 'DELETE' request to some restaurant
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=self.test_user2_token)
        response = client.post('/api/places/', self.restaurant_data, format='json')
        url = f"/api/places/{response.data['id']}/"

        client.credentials(HTTP_AUTHORIZATION=self.test_user1_token)
        response = client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class UsersAPITests(APITestCase):

    def test_get_token(self):
        """
        Test that user can get authorization 'token'
        """
        user_data = {
            'username': 'Einstein',
            'password': 'strongpsw123'
        }
        count_user_before = User.objects.count()
        count_token_before = Token.objects.count()

        url = '/api/users/'
        response = self.client.post(url, user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['token'] and type(response.data['token'] == str))

        self.assertEqual(User.objects.count(), count_user_before + 1)
        self.assertEqual(Token.objects.count(), count_token_before + 1)
