from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {})

def work(request):
    return render(request, 'main/work.html', {})

def contact(request):
    return render(request, 'main/contact.html', {})

def people(request):
    return render(request, 'main/people.html', {})

def about_us(request):
    return render(request, 'main/about_us.html', {})