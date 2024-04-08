from django import forms
from django.shortcuts import render


class UserContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    message = forms.CharField(widget=forms.Textarea)


def submit_contact_form(request):
    if request.method == 'POST':
        form = UserContactForm(request)
        if form.is_valid():
            # Data processing logic
            form = UserContactForm()
    else:
        form = UserContactForm()

    return render(request, 'submit_contact.html', {'form': form})
