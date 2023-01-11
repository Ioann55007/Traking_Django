from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import formset_factory



class ContactForm(forms.Form):
    name = forms.CharField()
    messages = forms.CharField(widget=forms.Textarea)

class TestContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)



class CommentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text_message = forms.CharField(widget=forms.Textarea)


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)


class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()


