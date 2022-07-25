from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from task_manager.users.models import User
from task_manager.tasks.models import Task


class LoginUserTest(TestCase):

    fixtures = ["users.json", "statuses.json", "tasks.json"]

    def setUp(self):
        self.user1 = User.objects.get(pk=5)
        self.user2 = User.objects.get(pk=6)

    def test_users(self):
        response = self.client.get(reverse('users:users'))
        users = list(response.context['users'])
        test_user1, test_user2 = users
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(test_user1.username, 'Test_user1')
        self.assertEqual(test_user2.username, 'Test_user2')

    def test_create_user(self):
        new_user = {
            'username': 'new_user',
            'first_name': '1',
            'last_name': '2',
            'password1': '123',
            'password2': '123',
        }
        response = self.client.post(
            reverse('users:create'),
            new_user,
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        created_user = User.objects.get(username=new_user['username'])
        self.assertTrue(created_user.check_password('123'))

    def test_update_user(self):
        self.client.force_login(self.user1)
        changed_data = {
            'username': self.user1.username,
            'first_name': '5',
            'last_name': self.user1.last_name,
            'password1': '777',
            'password2': '777',
        }
        response = self.client.post(
            reverse('users:update', args=(self.user1.id,)),
            changed_data,
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        changed_user = User.objects.get(username=self.user1.username)
        self.assertTrue(changed_user.check_password('777'))

    def test_delete_user(self):
        self.client.force_login(self.user1)
        Task.objects.all().delete()
        response = self.client.post(
            reverse('users:delete', args=(self.user1.id,)),
        )
        # noinspection PyTypeChecker
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(pk=self.user1.id)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
