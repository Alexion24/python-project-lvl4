from http import HTTPStatus
from django.test import Client, TestCase
from django.urls import reverse_lazy
from faker import Faker
from task_manager.statuses.models import Status
from task_manager.users.models import User


class StatusesTest(TestCase):

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
        self.name = self.faker.pystr()
        self.status = Status.objects.create(
            name=self.name,
        )
        self.status.save()

    def tearDown(self):
        self.user.delete()
        self.status.delete()

    def test(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse_lazy('statuses:statuses'),
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self._test_create_status()
        self._test_update_status(self.status)
        self._test_delete_status(self.status)

    def _test_create_status(self):
        response = self.client.post(
            reverse_lazy('statuses:create'),
            {'name': 'test_status'},
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def _test_update_status(self, status):
        response = self.client.post(
            reverse_lazy(
                'statuses:update',
                args=(status.id,),
            ),
            {'name': 'test'},
        )
        changed_status = Status.objects.get(name='test')
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(status.id, changed_status.id)

    def _test_delete_status(self, status):
        response = self.client.post(
            reverse_lazy(
                'statuses:delete',
                args=(status.id,),
            ),
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        with self.assertRaises(status.DoesNotExist):
            Status.objects.get(pk=status.id)
