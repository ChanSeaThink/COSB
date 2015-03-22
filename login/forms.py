from django import forms

class registForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField()
    nickname = forms.CharField()
