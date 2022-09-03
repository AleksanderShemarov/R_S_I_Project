from django.forms import ModelForm, CharField
# from django.contrib.auth.models import User
from django.contrib.auth.models import User


class UserFormReg(ModelForm):

    username = CharField(max_length=255, required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]
        # fields = "__all__"

        def __str__(self):
            return f"{self.model.first_name} {self.model.last_name}"


class UserEnter(ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]


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
