# coding: utf-8
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        # данные поля уже есть в UserCreationForm
        fields = (
                    'username'
                    , 'first_name'
                    , 'last_name'
                    , 'email'
                    , 'password1'
                    , 'password2'
        )
    # переопределяем процедуру сохранения
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)     # сохраняем родителя без коммита
        # получаем значения полей
        user.first_name = cleaned_data['first_name']
        user.last_name = cleaned_data['last_name']
        user.email = cleaned_data['email']

        # теперь можно сохранять
        if commit:
            user.save()
        return user
