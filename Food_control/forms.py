from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class CreateForm(forms.ModelForm):
    class Meta:
        model = User_table
        fields = ("food", "date", "image")
        labels = {
            "food": "飲食品項名稱",
            "date": "日期",
            "image": "圖片"
        }
        widgets = {
            # list="data-name" class="form-control" id="floatingInput
            'food': forms.TextInput(attrs={'class': 'form-control', 'list': 'data-name', 'id': 'floatingInput'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'datePicker'}),
            'image': forms.FileInput(
                attrs={'class': "form-control", 'id': "uploadImg", 'name': "filename", 'multiple accept': "image/*"})
        }


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="使用者名稱",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="確認密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(
        label="使用者名稱",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class SearchForm(forms.Form):
    search_date = forms.DateField(
        label="查詢日期",
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'datePicker'})
    )
