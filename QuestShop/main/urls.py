from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('work', views.work, name='work'),
    path('contact', views.contact, name='contact'),
    path('about', views.about_us, name='aboutus'),
    path('work', views.work, name='work'),
    path('people', views.people, name='people'),

]
