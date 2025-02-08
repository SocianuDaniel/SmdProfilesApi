from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from core import models
from django.contrib.auth.decorators import login_required
from core import forms


def register_owner(request):
    if request.method == "POST":
        form = forms.CreateNewUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            user, created  = get_user_model().objects.get_or_create(
                email=email, password=password1
                )
            if created:
                user.level = 1
                user.save()
                return redirect('owner:registration-complete')


        return render(request, 'owner/register.html', {'form': form})
    else:
        form = forms.CreateNewUserForm()
        return render(request, 'owner/register.html', {'form': form})

