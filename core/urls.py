from django.urls import include, path
from .views import home


# New (correct):
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('', views.home, name='home'),
]
