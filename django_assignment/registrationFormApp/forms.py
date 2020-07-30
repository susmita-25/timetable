from django import forms
#creating registration form

class RegistrationForm(forms.Form):
    Firstname = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control padding-class',
        'placeholder':'Firstname'
        }))
    Lastname = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control padding-class',
        'placeholder':'Lastname'
        }))
    # Mobile = forms.IntegerField(widget=forms.TextInput(attrs={
    #     'class':'form-control padding-class',
    #     'placeholder':'MobileNumber'
    #     }))
    Username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control padding-class',
        'placeholder':'Username'
        }))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control padding-class',
        'placeholder':'Password'
        }))

