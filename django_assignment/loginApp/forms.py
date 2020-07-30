from django import forms
#Creating a form
class LoginForm(forms.Form):
		username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control padding-class',
        'placeholder':'Username'
        }))
		password = forms.CharField(widget=forms.PasswordInput(attrs={
			'class':'form-control padding-class',
			'placeholder':'Password'
		}

		))