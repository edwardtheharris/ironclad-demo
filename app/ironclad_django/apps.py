from django.apps import AppConfig


class IroncladDjangoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ironclad_django"

from django.db import models
from django import forms
from django.core.validators import RegexValidator, EmailValidator
from django.shortcuts import render
from django.http import HttpResponse

# Models
class User(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=12,
        validators=[
            RegexValidator(
                regex=r'^\(\d{3}\) \d{3}-\d{4}$',
                message='Phone number must be in the format (XXX) XXX-XXXX',
            )
        ],
    )
    date_of_birth = models.DateField()

# Forms
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'date_of_birth']

    first_name = forms.CharField(
        max_length=50,
        required=True,
        validators=[RegexValidator(regex=r'^[a-zA-Z]+$', message='First name must contain only letters.')],
    )
    middle_name = forms.CharField(
        max_length=50,
        required=False,
        validators=[RegexValidator(regex=r'^[a-zA-Z]*$', message='Middle name must contain only letters.')],
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        validators=[RegexValidator(regex=r'^[a-zA-Z]+$', message='Last name must contain only letters.')],
    )
    email = forms.EmailField(
        required=True,
        validators=[EmailValidator(message='Enter a valid email address.')],
    )
    phone_number = forms.CharField(
        required=True,
        validators=[
            RegexValidator(
                regex=r'^\(\d{3}\) \d{3}-\d{4}$',
                message='Phone number must be in the format (XXX) XXX-XXXX',
            )
        ],
    )
    date_of_birth = forms.DateField(
        required=True,
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y'),
        error_messages={'invalid': 'Date of birth must be in MM/DD/YYYY format.'},
    )

# Views
def user_form_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User data saved successfully.")
        else:
            return render(request, 'user_form.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'user_form.html', {'form': form})

# Templates (user_form.html)
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Form</title>
</head>
<body>
    <h1>User Form</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

# Database settings in settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
