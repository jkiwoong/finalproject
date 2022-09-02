from pickle import TRUE
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=TRUE, help_text="필수 입력", label="아이디")
    email = forms.EmailField(max_length=254, help_text="필수 입력. 유효한 email주소를 입력하세요.", label="이메일")
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )
