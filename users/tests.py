from django.urls import reverse
from django.test import TestCase
from users.models import CustomUser


class RegistrationTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(
            reverse("users:register"),
            data={
                "username": "karaxanli",
                "first_name": "Polat",
                "last_name": "Alemdar",
                "email": "polat_alemdar@gmail.com",
                "password": "efe_karaxanli"
            }
        )

        user = CustomUser.objects.get(username="karaxanli")

        self.assertEqual(user.first_name, "Polat")
        self.assertEqual(user.last_name, "Alemdar")
        self.assertEqual(user.email, "polat_alemdar@gmail.com")
        self.assertNotEqual(user.password, "efe_karaxanli")
        self.assertTrue(user.check_password("efe_karaxanli"))

    def test_required_fields(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "first_name": "Polat",
                "email": "polat_alemdar@gmail.com"
            }
        )

        user_count = CustomUser.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "username", "This field is required.") # noqa
        self.assertFormError(response, "form", "password", "This field is required.") # noqa

    def test_invalid_email(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "username": "karaxanli",
                "first_name": "Polat",
                "last_name": "Alemdar",
                "email": "invalid-email",
                "password": "efe_karaxanli"
            }
        )

        user_count = CustomUser.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "email", "Enter a valid email address.") # noqa

    def test_unique_username(self):
        user = CustomUser.objects.create(username="karaxanli", first_name="Polat") # noqa
        user.set_password("somepass")
        user.save()

        response = self.client.post(
            reverse("users:register"),
            data={
                "username": "karaxanli",
                "first_name": "Polat",
                "last_name": "Alemdar",
                "email": "polat_alemdar@gmail.com",
                "password": "efe_karaxanli"
            }
        )

        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 1)
        self.assertFormError(response, "form", "username", "A user with that username already exists.") # noqa
