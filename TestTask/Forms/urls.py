from django.urls import path
from .views import get_forms_view

urlpatterns = [
    path('get_form/', get_forms_view, name='get_form'),
]
