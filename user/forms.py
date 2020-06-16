from django import forms
from user.models import Post



class product_form(forms.ModelForm):
	name                = forms.CharField(widget = forms.TextInput({'placeholder':'Your Title'}))
	email               = forms.EmailField(widget = forms.TextInput({'placeholder':'Enter Email id'}))
	discription         = forms.CharField(required = False , widget = forms.Textarea({

														'class' : "new-class",
														'rows' : 5,'placeholder': ' your Discription','cols':20

																		}))
	author              = forms.CharField(widget = forms.TextInput({'placeholder':'Your full name'}))

	class Meta:
		model = Post
		fields = [
		'name',
		'email',
		'discription',
		'author'
		]