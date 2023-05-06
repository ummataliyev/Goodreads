from django.views import View
from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from users.forms import UserCreateForm
from django.contrib.auth.forms import AuthenticationForm


class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {
            "form": create_form
        }

        return render(request, "users/register.html", context=context)

    def post(self, request):
        create_form = UserCreateForm(request.POST)

        if create_form.is_valid():
            user = create_form.save()
            user.set_password(create_form.cleaned_data['password'])
            user.save()
            return redirect('users:login')
        else:
            context = {
                "form": create_form
            }
            return render(request, "users/register.html", context)


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()

        return render(request, "users/login.html", {"login_form": login_form})

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)

            return redirect("landing_page")

        else:
            return render(request, "users/login.html", {"login_form": login_form}) # noqa
