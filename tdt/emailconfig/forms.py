from django import forms
from authentication.models import User,AdminUser,NormalUser
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from tdt.settings import ALLOWED_SIGNUP_DOMAINS
from .models import FetchParentRequest

def SignupDomainValidator(value):
    if '*' not in ALLOWED_SIGNUP_DOMAINS:
        try:
            domain = value[value.index("@"):]
            if domain not in ALLOWED_SIGNUP_DOMAINS:
                raise ValidationError('Invalid domain. Allowed domains on this network: {0}'.format(','.join(ALLOWED_SIGNUP_DOMAINS)))  # noqa: E501

        except Exception:
            raise ValidationError('Invalid domain. Allowed domains on this network: {0}'.format(','.join(ALLOWED_SIGNUP_DOMAINS)))  # noqa: E501


def UniqueEmailValidator(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError('User with this Email already exists.')

def ParentEmailValidator(value):
    if User.objects.filter(email__iexact=value).exists() == False:
        raise ValidationError('Parent Email does not exists.')



class FetchParentForm(forms.ModelForm):
    your_email = forms.CharField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter your email address"}),
        required=True,
        max_length=75)
    parent_email = forms.CharField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter parent email address"}),
        required=True,
        max_length=75)

    class Meta:
        model = FetchParentRequest
        fields = ['your_email', 'parent_email']

    def __init__(self, *args, **kwargs):
        super(FetchParentForm, self).__init__(*args, **kwargs)
        self.fields['your_email'].validators.append(UniqueEmailValidator)
        self.fields['your_email'].validators.append(SignupDomainValidator)
        self.fields['parent_email'].validators.append(SignupDomainValidator)
        self.fields['parent_email'].validators.append(ParentEmailValidator)