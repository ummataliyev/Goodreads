from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from users.forms import UserLoginForm
from users.forms import UserCreateForm
from django.contrib.auth.models import User


class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {
            "form": create_form
        }

        return render(request, "users/register.html", context=context)

    def post(self, request):
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            )

        user.set_password(password)
        user.save()

        # create user account
        return redirect('users:login')


class LoginView(View):
    def get(self, request):
        login_form = UserLoginForm()

        return render(request, "users/login.html", {"login_form": login_form})

    def post(self, request):
        login_form = UserLoginForm(data=request.POST)

        if login_form.is_valid():
            # log in the user
            pass
        else:
            return render(request, "users/login.html", {"login_form": login_form}) # noqa
