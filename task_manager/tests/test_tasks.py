from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status


class TasksTest(TestCase):

    fixtures = ["users.json", "statuses.json", "tasks.json"]

    def setUp(self):
        self.task1 = Task.objects.get(pk=7)
        self.task2 = Task.objects.get(pk=8)

        self.user1 = User.objects.get(pk=5)
        self.user2 = User.objects.get(pk=6)

        self.status1 = Status.objects.get(pk=6)
        self.status2 = Status.objects.get(pk=7)

    def test_tasks(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('tasks:tasks'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        tasks = list(response.context['tasks'])
        self.assertQuerysetEqual(tasks, [self.task1, self.task2])

    def test_create_task(self):
        self.client.force_login(self.user1)
        new_task = {
            'name': 'test_task3',
            'description': '123',
            'status': 6,
            'author': 5,
            'executor': 5,
        }
        response = self.client.post(
            reverse('tasks:create'),
            new_task
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        created_task = Task.objects.get(name=new_task['name'])
        self.assertEquals(created_task.name, 'test_task3')

    def test_update_task(self):
        self.client.force_login(self.user1)
        changed_data = {
            'name': 'test',
            'description': '777',
            'status': 6,
            'author': 5,
            'executor': 5,
        }
        response = self.client.post(
            reverse('tasks:update', args=(self.task1.id,)),
            changed_data,
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        changed_task = Task.objects.get(name='test')
        self.assertEqual(self.task1.id, changed_task.id)

    def test_delete_task(self):
        self.client.force_login(self.user1)
        response = self.client.post(
            reverse(
                'tasks:delete',
                args=(self.task1.id,),
            ),
        )
        # noinspection PyTypeChecker
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(pk=self.task1.id)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
