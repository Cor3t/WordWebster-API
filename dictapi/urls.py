from django.urls import path
from . import views

urlpatterns = [
    path('dict', views.dict_list, name='dictionary')
]