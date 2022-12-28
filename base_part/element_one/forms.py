from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import User
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    name = forms.CharField()
    messages = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        pass


class CommentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text_message = forms.CharField(widget=forms.Textarea)


class AuthorInterestForm(forms.Form):
    message = forms.CharField()


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)











