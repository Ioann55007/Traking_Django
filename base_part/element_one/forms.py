from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    messages = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        pass
