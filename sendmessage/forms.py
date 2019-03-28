from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'w3-input w3-border', 'placeholder' : 'Name'}), required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'w3-input w3-border', 'placeholder' : 'Email'}), required=True)
    message = forms.CharField(widget=forms.TextInput(attrs={'class' : 'w3-input w3-border', 'placeholder' : 'Message'}),  required=True)