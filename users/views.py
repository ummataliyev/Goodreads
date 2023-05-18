from django.views import View
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from users.forms import UserUpdateForm
from users.forms import UserCreateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin


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

            messages.success(request, "You have successfully logged in :)")

            return redirect("landing_page")

        else:
            return render(request, "users/login.html", {"login_form": login_form}) # noqa


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "users/profile.html", {"user": request.user})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully loged out :)")
        return redirect("landing_page")


class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        user_update_form = UserUpdateForm(instance=request.user)
        return render(request, "users/profile_edit.html", {"form": user_update_form}) # noqa

    def post(self, request):
        user_update_form = UserUpdateForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
            )

        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, "You have succesfully updated your profile ;)") # noqa

            return redirect("users:profile")

        return render(request, "users/profile_edit.html", {"form": user_update_form}) # noqa
