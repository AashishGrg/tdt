from django import forms
from authentication.models import User,AdminUser,NormalUser
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from tdt.settings import ALLOWED_SIGNUP_DOMAINS


def SignupDomainValidator(value):
    if '*' not in ALLOWED_SIGNUP_DOMAINS:
        try:
            domain = value[value.index("@"):]
            if domain not in ALLOWED_SIGNUP_DOMAINS:
                raise ValidationError('Invalid domain. Allowed domains on this network: {0}'.format(','.join(ALLOWED_SIGNUP_DOMAINS)))  # noqa: E501

        except Exception:
            raise ValidationError('Invalid domain. Allowed domains on this network: {0}'.format(','.join(ALLOWED_SIGNUP_DOMAINS)))  # noqa: E501

# these user name are not allowed
def ForbiddenUsernamesValidator(value):
    forbidden_usernames = ['admin', 'settings', 'news', 'about', 'help',
                           'signin', 'signup', 'signout', 'terms', 'privacy',
                           'cookie', 'new', 'login', 'logout', 'administrator',
                           'join', 'account', 'username', 'root', 'blog',
                           'user', 'users', 'billing', 'subscribe', 'reviews',
                           'review', 'blog', 'blogs', 'edit', 'mail', 'email',
                           'home', 'job', 'jobs', 'contribute', 'newsletter',
                           'shop', 'profile', 'register', 'auth',
                           'authentication', 'campaign', 'config', 'delete',
                           'remove', 'forum', 'forums', 'download',
                           'downloads', 'contact', 'blogs', 'feed', 'feeds',
                           'faq', 'intranet', 'log', 'registration', 'search',
                           'explore', 'rss', 'support', 'status', 'static',
                           'media', 'setting', 'css', 'js', 'follow',
                           'activity', 'questions', 'articles', 'network',
                           'search']

    if value.lower() in forbidden_usernames:
        raise ValidationError('This is a reserved word.')


def InvalidUsernameValidator(value):
    if '@' in value or '+' in value or '-' in value:
        raise ValidationError('Enter a valid username.')


def UniqueEmailValidator(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError('User with this Email already exists.')


def UniqueUsernameIgnoreCaseValidator(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError('User with this Username already exists.')


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(
          widget=forms.TextInput(
              attrs={"class": "text-info", "placeholder": " Enter your first name"}),
          max_length=30,
          required=True,)
    last_name = forms.CharField(
          widget=forms.TextInput(
              attrs={"class": "text-info", "placeholder": " Enter your last name"}),
          max_length=30,
          required=True,)
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "text-info", "placeholder": " Enter your username"}),
        max_length=30,
        required=True,)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "text-info", "placeholder": "Enter the password"}))
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter your email address"}),
        required=True,
        max_length=75)

    class Meta:
        model = User
        exclude = ['last_login', 'date_joined']
        fields = ['first_name','last_name','username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(ForbiddenUsernamesValidator)
        self.fields['username'].validators.append(InvalidUsernameValidator)
        self.fields['username'].validators.append(
            UniqueUsernameIgnoreCaseValidator)
        self.fields['email'].validators.append(UniqueEmailValidator)
        self.fields['email'].validators.append(SignupDomainValidator)

    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('password')
        return self.cleaned_data

class AdminSignUpForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "text-info", "placeholder": " Enter your username"}),
        max_length=30,
        required=True,)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "text-info", "placeholder": "Enter the password"}))
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter your email address"}),
        required=True,
        max_length=75)

    class Meta:
        model = AdminUser
        fields = ['username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(AdminSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(ForbiddenUsernamesValidator)
        self.fields['username'].validators.append(InvalidUsernameValidator)
        self.fields['username'].validators.append(
            UniqueUsernameIgnoreCaseValidator)
        self.fields['email'].validators.append(UniqueEmailValidator)
        self.fields['email'].validators.append(SignupDomainValidator)

    def clean(self):
        super(AdminSignUpForm, self).clean()
        password = self.cleaned_data.get('password')
        return self.cleaned_data

class NormalUserSignUpForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "text-info", "placeholder": " Enter your username"}),
        max_length=30,
        required=True,)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "text-info", "placeholder": "Enter the password"}))
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter your email address"}),
        required=True,
        max_length=75)
    parent_code = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your parent_code"}),
        required=True,
        max_length=16)

    class Meta:
        model = User
        fields = ['username', 'email', 'password','parent_code']

    def __init__(self, *args, **kwargs):
        super(NormalUserSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(ForbiddenUsernamesValidator)
        self.fields['username'].validators.append(InvalidUsernameValidator)
        self.fields['username'].validators.append(
            UniqueUsernameIgnoreCaseValidator)
        self.fields['email'].validators.append(UniqueEmailValidator)
        self.fields['email'].validators.append(SignupDomainValidator)

    def clean(self):
        super(NormalUserSignUpForm, self).clean()
        password = self.cleaned_data.get('password')
        return self.cleaned_data

