from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user


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


        user_count = User.objects.count()
        user=User.objects.get(username="abdulaziz")

        self.assertEqual(user_count, 1)
        self.assertEqual(user.first_name, "Abdulaziz")
        self.assertEqual(user.last_name, "Sultonmahmudov")
        self.assertEqual(user.email, "abdulaziz@gmail.com")
        self.assertNotEqual(user.password, "1234")
        self.assertTrue(user.check_password("1234"))


    def test_username_field(self):
        response  = self.client.post(
            reverse('users:register'),
            data={
                "username": "root",
                "first_name": "Abdulaziz",
                "last_name": "Sultonmahmudov",
                "email": "abdulaziz@gmail.com",
                "password": "1234",
                "password_confirm": "1234"
            }
        )

        form = response.context['form']

        user_count = User.objects.count()
        self.assertEqual(user_count,0)
        self.assertEqual(form.errors)
        self.assertIn("username", form.errors.keys())
        self.assertEqual(form.errors ['username'],["Username 5 va 30 orasida bolishi lozim"])
        


    def test_password_field(self):

        response  = self.client.post(
            reverse('user:register'),
            data={
                "username": "abdulaziz",
                "first_name": "Abdulaziz",
                "last_name": "Sultonmahmudov",
                "email": "abdulaziz@gmail.com",
                "password": "12343549",
                "password_confirm": "1234"
            }
        )

        form = response.context['form']

        user_count = User.objects.count()
        self.assertEqual(user_count,0)
        self.assertEqual(form.errors)
        self.assertIn("password_confirm" , form.errors.keys())
        self.assertEqual(form.errors['password_confirm'],["Passwordlar bir biriga mos emas"])


    def test_email_field(self):

        response  = self.client.post(
            reverse('user:register'),
            data={
                "username": "abdulaziz",
                "first_name": "Abdulaziz",
                "last_name": "Sultonmahmudov",
                "email": "abdulaziz459",
                "password": "12343549",
                "password_confirm": "1234"
            }
        )

        form = response.context['form']

        user_count = User.objects.count()
        self.assertEqual(user_count,0)
        self.assertEqual(form.errors)
        self.assertIn("email", form.errors.keys())
        self.assertEqual(form.errors['email'],["Enter a valid email address."])





class LoginTestCase(TestCase):

    def test_login_success(self):
       user = User.objects.create(username="abdulaziz", first_name="Abdulaziz", last_name="Sallimahmudov")
       user.set_password("1234")

       user.save()



       self.client.post(
           reverse('user:login'),
           data={
               "username": "abdulaziz",
               "password": "1234"
           }
        )
       
       user_count = User.objects.count()
       self.assertEqual(user_count,1)

       user = get_user(self.client)
       self.assertTrue(user.is_authenticated)


    def test_username_field(self):

        self.client.post(
        data={
               "username": "abdulaziz",
               "password": "1234"
           }
        )
        form = self.client.context['form']
        user_count = User.objects.count()
        self.assertEqual(user_count,0)
        self.assertEqual(form.errors)
        self.assertIn("username", form.errors.keys())
        self.assertEqual(form.errors ['username'],["Username 5 va 30 orasida bolishi lozim"])
        


