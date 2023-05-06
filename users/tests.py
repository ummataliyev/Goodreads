from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User


class RegistrationView(TestCase):
    def test_user_account_is_created(self):
        self.client.post(
            reverse("users:register"),
            data={
                "username": "djohn",
                "first_name": "Umidjon",
                "last_name": "Ummataliyev",
                "email": "djohn_ummataliyev@gmail.com",
                "password": "somepassword"
                }
            )

        user = User.objects.get(username="djohn")

        self.assertEqual(user.first_name, "Umidjon")
        self.assertEqual(user.last_name, "Ummataliyev")
        self.assertEqual(user.email, "djohn_ummataliyev@gmail.com")
        self.assertNotEqual(user.password, "somepassword")
        self.assertTrue(user.check_password("somepassword"))

    def test_required_fields(self):
        self.client.post(
            reverse("users:register"),
            data={
                "first_name": "Umidjon",
                "email": "djohn_ummataliyev@gmail.com"
            }
        )

        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
