from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.labels.models import Label


class TestLabel(TestCase):

    fixtures = ["users.json", "statuses.json", "tasks.json", 'labels.json']

    def setUp(self):
        self.label1 = Label.objects.get(pk=1)
        self.label2 = Label.objects.get(pk=2)
        self.label3 = Label.objects.get(pk=3)
        self.label4 = Label.objects.get(pk=4)
        self.status1 = Status.objects.get(pk=6)
        self.task1 = Task.objects.get(pk=7)
        self.user = User.objects.get(pk=5)

    def test_labels(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('labels:labels'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        labels_list = list(response.context['labels'])
        self.assertQuerysetEqual(
            labels_list,
            [
                self.label1,
                self.label2,
                self.label3,
                self.label4,
            ],
        )

    def test_create_label(self):
        self.client.force_login(self.user)
        new_label = {'name': "test_label5"}
        response = self.client.post(reverse('labels:create'), new_label)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        created_label = Label.objects.get(name=new_label['name'])
        self.assertEquals(created_label.name, "test_label5")

    def test_update_label(self):
        self.client.force_login(self.user)
        changed_data = {'name': "changed"}
        response = self.client.post(
            reverse('labels:update', args=(self.label1.pk,)),
            changed_data
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Label.objects.get(pk=self.label1.id), self.label1)

    def test_delete_label_is_use(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('labels:delete', args=(self.label1.pk,))
        )
        self.assertTrue(Label.objects.filter(pk=self.label1.id).exists())
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_delete_label(self):
        self.client.force_login(self.user)
        Task.objects.all().delete()
        response = self.client.post(
            reverse('labels:delete', args=(self.label1.pk,))
        )
        # noinspection PyTypeChecker
        with self.assertRaises(Label.DoesNotExist):
            Label.objects.get(pk=self.label1.pk)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
