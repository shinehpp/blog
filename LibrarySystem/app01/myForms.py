from django import forms
from django.forms import widgets


class UserForm(forms.Form):
	name = forms.CharField(min_length=4, label='用户名', widget=widgets.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(min_length=6,widget=widgets.PasswordInput(attrs={'class': 'form-control'}))
	re_password = forms.CharField(min_length=6, label='确认密码', widget=widgets.TextInput(attrs={'class': 'form-control'}))
	tel = forms.CharField(max_length=11, label='手机号', widget=widgets.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(label='Email', widget=widgets.TextInput(attrs={'class': 'form-control'}))
