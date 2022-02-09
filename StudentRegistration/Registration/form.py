from django import forms
from Registration.models import RegistrationStu

class StuRegistration(forms.ModelForm):
    class Meta:
        model=RegistrationStu
        fields=['name','email','password']
        Widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }