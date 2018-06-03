from django import forms
from .models import NewsUsers
class NewsUserForm(forms.ModelForm):
	class Meta:
		model = NewsUsers
		fields = ['email','name']