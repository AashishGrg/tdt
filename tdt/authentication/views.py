from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from authentication.models import User,AdminUser,NormalUser
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import SignUpForm, AdminSignUpForm,NormalUserSignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
import random
import string


class UserSignupForm(View):
    form_class = SignUpForm
    template_name = 'signup.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            code = ''.join(random.choices(
                string.ascii_letters + string.digits, k=16))
            user.code = code
            print(user.code)
            user.save()
            # returns these objects if credential are correct
            user = authenticate(username=username, password=password)
            # if user is not None:
            #     if user.is_active:
            #         login(request, user)
            #         # after signup redirect to profile settings
            #         return redirect('authentication:login')

        return render(request, self.template_name, {'form': form})


class AdminUserSignupForm(View):
    form_class = SignUpForm
    template_name = 'admin_signup.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            user.code = code
            user.save()
            admin = AdminUser.objects.create(admin_user=user)
            admin.save()
            # returns these objects if credential are correct
            user = authenticate(username=username, password=password)
            # if user is not None:
            #     if user.is_active:
            #         login(request, user)
            #         # after signup redirect to profile settings
            #         return redirect('authentication:login')
        return render(request, self.template_name, {'form': form})

class NormalUserSignupForm(View):
    form_class = NormalUserSignUpForm
    template_name = 'normal_user_signup.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            parent_code = form.cleaned_data['parent_code']
            user.set_password(password)
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            user.code = code
            user.save()
            parent_user = User.objects.get(code = parent_code)
            parent_user_code = parent_user.code
            if parent_user_code==parent_code:
            	normal_user = NormalUser.objects.create(user=user,parent_user=parent_user,parent_code=parent_code)
            	normal_user.save()
            user = authenticate(username=username, password=password)
            # if user is not None:
            #     if user.is_active:
            #         login(request, user) 
            #         # after signup redirect to profile settings
            #         return redirect('authentication:login')
        return render(request, self.template_name, {'form': form})

def logout_view(request):
    logout(request)
    return redirect('authentication:login')

