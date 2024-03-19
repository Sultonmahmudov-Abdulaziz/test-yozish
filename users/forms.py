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



class LoginForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['password'] = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=('username', 'password')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("Bu foydalanuvchi nomi mavjud emas")
        return username


    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        
        user =authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Foydalanuvchi nomi yoki parol xato")
        
        return cleaned_data