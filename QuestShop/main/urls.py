from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('work', views.work, name='work'),
    path('work/<int:work_id>/', views.detail, name='detail'),
    path('contact', views.contact, name='contact'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
