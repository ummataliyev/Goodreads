from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user
from django.contrib.auth.models import CustomUser


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
        user = User.objects.create(username="karaxanli", first_name="Polat") # noqa
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


class LoginTestCase(TestCase):
    def setUp(self):
        self.db_user = CustomUser.objects.create(username='karaxanli', first_name="Polat") # noqa
        self.db_user.set_password("efe_karaxanli")
        self.db_user.save()

    def test_successful_login(self):
        self.client.post(
            reverse("user:login"),
            data={
                "username": "karaxanli",
                "password": "efe_karaxanli"
            }
        )

        user = get_user(self.client)

        self.assertTrue(user.is_authenticated)

    def test_wrong_creditials(self):
        self.client.post(
            reverse("user:login"),
            data={
                "username": "karaxanli",
                "password": "wrongpassword"
            }
        )

        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def test_logout(self):
        self.client.login(username='karaxanli', password='efe_karaxanli')

        self.client.get(reverse("users:logout"))

        user = get_user(self.client)

        self.assertFalse(user.is_authenticated)


class ProfileTestCase(TestCase):
    def test_login_required(self):
        response = self.client.get(reverse("user:profile"))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("users:login") + "?next=/users/profile/") # noqa

    def test_profile_detail(self):
        user = CustomUser
        .objects.create(
            username="karaxanli",
            first_name="Polat",
            last_name="Alemdar",
            email="polat_alemdar@gmail.com"
        )
        user.set_password("efe_karaxanli")
        user.save()

        self.client.login(username="polat", password="efe_karaxanli")
        response = self.clientget(reverse("users:profile"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, user.username)
        self.assertContains(response, user.first_name)
        self.assertContains(response, user.last_name)
        self.assertContains(response, user.email)
