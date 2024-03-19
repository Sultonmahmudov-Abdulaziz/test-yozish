from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class RegisterTestCase(TestCase):

    def test_register_success(self):
        self.client.post(
            reverse('user:register'),
            data={
                "username": "abdulaziz",
                "first_name": "Abdulaziz",
                "last_name": "Sultonmahmudov",
                "email": "abdulaziz@gmail.com",
                "password": "1234",
                "password_confirm": "1234"
            }
        )


        user_count = User.objects.all().count()
        user=User.objects.get(username="abdulaziz")

        self.assertEqual(user_count, 1)
        self.assertEqual(user.first_name, "Abdulaziz")
        self.assertEqual(user.last_name, "Sultonmahmudov")
        self.assertEqual(user.email, "abdulaziz@gmail.com")
        self.assertNotEqual(user.password, "1234")
        self.assertTrue(user.check_password("1234"))




class LoginTestCase(TestCase):

    def test_login_success(self):
        self.client.post(
            reverse('user:login'),
            data={
                "username": "abdulaziz",
                "password": "0102"
            }
        )

        user_count=User.objects.all().count()
        user=User.objects.get(username="abdulaziz")
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user.password, "0102")
        self.assertTrue(user.check_password("0102"))
        