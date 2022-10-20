from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from users.models import UserInfo


class TestUserInfo(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create(username="testuser1")

    def test_create_user_info(self):
        UserInfo.objects.create(
            user=self.user,
            first_name="Miki",
            last_name="Mica",
        )

        self.assertTrue(UserInfo.objects.filter(first_name="Miki").exists())


class TestGetUserInfoAPI(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(username="testuser2")
        self.user_no_info = get_user_model().objects.create(username="testuser3")
        self.user_info = UserInfo.objects.create(user=self.user, first_name="Test", last_name="Ltest", email="hey@test.com")
        self.url = reverse("users:info")
        self.client_with_info = APIClient()
        self.client_with_info.force_login(self.user)
        self.client_no_info = APIClient()
        self.client_no_info.force_login(self.user_no_info)

    def test_get_user_info(self) -> None:
        response = self.client_with_info.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_no_info(self) -> None:
        response = self.client_no_info.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_user_info_no_auth_user(self) -> None:
        client = APIClient()
        response = client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_user_first_name(self):
        response = self.client_with_info.patch(self.url, {"first_name": "John", "email": "test@email.com"})
        self.user_info.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user_info.email, "test@email.com")
        self.assertEqual(self.user_info.first_name, "John")
