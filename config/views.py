from django .shortcuts import render



def landing_page(request):
    return render(request, template_name= 'landing.html')