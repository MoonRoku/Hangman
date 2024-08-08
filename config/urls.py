from django.contrib import admin
from django.urls import include, path
from django.views.generic import *
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    
]