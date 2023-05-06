from django import forms


class UserCreateForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=250)
    password = forms.CharField(max_length=128)
