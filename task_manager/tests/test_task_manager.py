from http import HTTPStatus
from django.template.response import TemplateResponse
from django.test import Client, TestCase
from django.urls import reverse_lazy
from faker import Faker
from task_manager.users.forms import CreateUserForm
from task_manager.users.models import User


class IndexPageViewTest(TestCase):

    def test_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)


class RegistrationPageViewTest(TestCase):

    def setUp(self):
        self.client: Client = Client()

    def test(self):
        response: TemplateResponse = self.client.get(
            reverse_lazy('users:create'),
        )
        form_fields = CreateUserForm.base_fields
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self._assert_first_name(form_fields, response)
        self._assert_last_name(form_fields, response)
        self._assert_username(form_fields, response)
        self._assert_password(form_fields, response)
        self._assert_password_confirmation(form_fields, response)

    def _assert_first_name(self, form_fields, response):
        self.assertIn(
            str(form_fields['first_name'].label),
            response.rendered_content,
        )
        self.assertIn(
            str(form_fields['first_name'].help_text),
            response.rendered_content,
        )

    def _assert_last_name(self, form_fields, response):
        self.assertIn(
            str(form_fields['last_name'].label),
            response.rendered_content,
        )
        self.assertIn(
            str(form_fields['last_name'].help_text),
            response.rendered_content,
        )

    def _assert_username(self, form_fields, response):
        self.assertIn(
            str(form_fields['username'].label),
            response.rendered_content,
        )
        self.assertIn(
            str(form_fields['username'].help_text),
            response.rendered_content,
        )

    def _assert_password(self, form_fields, response):
        self.assertIn(
            str(form_fields['password1'].label),
            response.rendered_content,
        )
        self.assertIn(
            str(form_fields['password1'].help_text),
            response.rendered_content,
        )

    def _assert_password_confirmation(self, form_fields, response):
        self.assertIn(
            str(form_fields['password2'].label),
            response.rendered_content,
        )
        self.assertIn(
            str(form_fields['password2'].help_text),
            response.rendered_content,
        )


class SuccessRegistrationTest(TestCase):

    def setUp(self):
        self.faker = Faker()
        self.client = Client()

    def test(self):
        first_name = self.faker.first_name()
        last_name = self.faker.last_name()
        username = self.faker.user_name()
        password = self.faker.password()
        response = self.client.post(
            reverse_lazy('users:create'),
            data={
                'first_name': first_name,
                'last_name': last_name,
                'username': username,
                'password1': password,
                'password2': password,
            },
        )
        self.assertRedirects(response, reverse_lazy('login'))
        self.assertTrue(
            User.objects.filter(first_name=first_name, username=username),
        )
