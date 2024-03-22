from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password_confirm'] = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email', 'password')



    def clean_password_confirm(self):
        password=self.cleaned_data['password']
        password_confirm=self.cleaned_data['password_confirm']


        if password!= password_confirm:
            raise forms.ValidationError("Passwordlar bir biriga mos emas")
        
        return password
    
    def clean_username(self):
        username=self.cleaned_data['username']


        if len(username) <5 or len(username) >30:
            raise forms.ValidationError("Username 5 va 30 orasida bolishi lozim")
        

        return username



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username=self.cleaned_data['username']


        if len(username) <5 or len(username) >30:
            raise forms.ValidationError("Username 5 va 30 orasida bolishi lozim")
        

        return username
        
   
    

   