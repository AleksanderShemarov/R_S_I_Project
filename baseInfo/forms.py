from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserFormReg(forms.ModelForm):

    username = forms.CharField(max_length=255, required=False)
    password_first = forms.CharField(label="Your password", widget=forms.PasswordInput)
    password_second = forms.CharField(label="Repeat it", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]
        # fields = "__all__"

        def is_common(self):
            datum = self.cleaned_data
            if datum['password_first'] != datum['password_second']:
                raise forms.ValidationError('Passwords aren\'t the same.')
            return datum['password_second']


# class UserEnter(forms.ModelForm):
#
#     # email = forms.EmailField(label="Enter email", widget=forms.EmailInput)
#     # password = forms.CharField(label="Password", widget=forms.PasswordInput)
#     username = forms.CharField(label="Your nickname", max_length=255)
#
#     class Meta:
#         model = User
#         fields = ['username']


class AuthUserForm(AuthenticationForm, forms.ModelForm):

    class Meta:
        model = User
        fields = ["username", "email", "password"]


# class Registration(forms.Form):
#
#     username = forms.CharField(required=False, label="Your nickname, if you want")
#     name = forms.CharField(label="Your name")
#     surname = forms.CharField(label="Your surname")
#     email = forms.EmailField(label="post@org.com")
#
#     class Meta:
#
#         model = User
#         fields = "__all__"  # ["name", "surname", "surname", "username"]
