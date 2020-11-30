from django.urls import path
from .views import query_output

urlpatterns = [
    path('', query_output, name='home'),
]