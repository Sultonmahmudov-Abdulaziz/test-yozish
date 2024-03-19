from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterForm,LoginForm


class RegisterView(View):

    def get(self, request):

        form=RegisterForm()
        return render(request, template_name= 'users/register.html', context={'form': form})
    



    def post(self, request):
        form=RegisterForm(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('landing_page')


        return render(request, template_name= 'users/register.html', context={'form': form})
    


class LoginView(View):
    def get(self, request):
        form=LoginForm()
        return render(request, template_name= 'users/login.html', context={'form': form})
    


    def post(self, request):
        form=LoginForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('landing_page')
        
        return render(request, template_name= 'users/login.html', context={'form': form})
       

