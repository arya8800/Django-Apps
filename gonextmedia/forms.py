from django import forms
from gonextmedia.models import *
from django.core.exceptions import ValidationError


class user(forms.Form):
	firstname = forms.CharField()
	lastname = forms.CharField()
	pwd1 = forms.CharField(widget=forms.PasswordInput(),required=False)
	pwd2 = forms.CharField(widget=forms.PasswordInput(),required=False)
	email = forms.EmailField()
	
