from http import HTTPStatus
from django.test import Client, TestCase
from task_manager.users.models import User
from django.urls import reverse_lazy
from faker import Faker


class LoginUserTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.faker = Faker()
        self.username = self.faker.user_name()
        self.password = self.faker.password(length=5)
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
        )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test(self):
        response = self.client.get(
            reverse_lazy('login'),
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self._test_correct()
        self._test_wrong_password()
        self._test_wrong_username()

    def _test_correct(self):
        response = self.client.post(
            '/login/',
            {
                'username': self.username,
                'password': self.password,
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def _test_wrong_username(self):
        response = self.client.post(
            '/login/',
            {
                'username': 'wrong_username',
                'password': self.password,
            },
        )
        self.assertFalse(response.status_code == HTTPStatus.FOUND)

    def _test_wrong_password(self):
        response = self.client.post(
            '/login/',
            {
                'username': self.username,
                'password': 'wrong_password',
            },
        )
        self.assertFalse(response.status_code == HTTPStatus.FOUND)
