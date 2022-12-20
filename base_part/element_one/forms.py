from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    messages = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        pass


class CommentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text_message = forms.CharField(widget=forms.Textarea)
