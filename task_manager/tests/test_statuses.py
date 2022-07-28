from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.tasks.models import Task


class StatusesTest(TestCase):

    fixtures = ["users.json", "statuses.json", "tasks.json", 'labels.json']

    def setUp(self):
        self.user = User.objects.get(pk=5)
        self.status1 = Status.objects.get(pk=6)
        self.status2 = Status.objects.get(pk=7)

    def test_statuses(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('statuses:statuses'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        statuses = list(response.context['statuses'])
        self.assertQuerysetEqual(statuses, [self.status1, self.status2])

    def test_create_status(self):
        self.client.force_login(self.user)
        new_status = {'name': 'test_status3'}
        response = self.client.post(
            reverse('statuses:create'),
            new_status,
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        created_status = Status.objects.get(name=new_status['name'])
        self.assertEqual(created_status.name, 'test_status3')

    def test_update_status(self):
        self.client.force_login(self.user)
        changed_data = {'name': 'test'}
        response = self.client.post(
            reverse(
                'statuses:update',
                args=(self.status1.id,),
            ),
            changed_data,
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        changed_status = Status.objects.get(name='test')
        self.assertEqual(self.status1.id, changed_status.id)

    def test_delete_status(self):
        self.client.force_login(self.user)
        Task.objects.all().delete()
        response = self.client.post(
            reverse('statuses:delete', args=(self.status1.id,)),
        )
        # noinspection PyTypeChecker
        with self.assertRaises(Status.DoesNotExist):
            Status.objects.get(pk=self.status1.id)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
