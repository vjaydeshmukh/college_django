from django import forms


class loginForm(forms.Form):
    username = forms.CharField(required=True, empty_value=False, label='Username', max_length=150)
    password = forms.CharField(widget=forms.PasswordInput(), required=True, empty_value=False, label='Password', max_length=100)
