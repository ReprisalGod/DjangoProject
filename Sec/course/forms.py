from django import forms
class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    roll = forms.IntegerField()
    city = forms.CharField(max_length=100)
    marks = forms.IntegerField()
    