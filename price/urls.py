from django.urls import path
from . import views

urlpatterns = [
    path('<id>', views.price_evaluation, name='price_evaluation'),
]
