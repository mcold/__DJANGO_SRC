# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm     # 17 


# Create your views here.

def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = 'Michael Cold Superman'

    args = {'myName': name}
    return render(request, 'accounts/home.html', args)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = RegistrationForm()           # 17 меняем на собственную форму
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)