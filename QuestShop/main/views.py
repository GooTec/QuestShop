from django.shortcuts import render, HttpResponseRedirect , get_object_or_404
from .models import MainImg, Work, Contact, ContactForm


# Create your views here.
def index(request):
    mains = MainImg.objects.all()
    return render(request, 'main/index.html', {'mains':mains})

def work(request):
    works = Work.objects.all()
    return render(request, 'main/work.html', {'works' : works})

def detail(request, work_id):
    work = get_object_or_404(Work, pk=work_id)
    return render(request, 'main/detail.html', {'work': work})


def contact(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/')

            # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})

