from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .constants import *


# Create your views here.

def price_evaluation(request, id):
    constraint_data = Constraints.objects.get(id=id)
    price = 0
    if constraint_data.distance_covered <= BASE_DISTANCE:
        price = DBP * constraint_data.time_taken
    else:
        price = (DBP + (constraint_data.distance_covered - BASE_DISTANCE) * DAP) * constraint_data.time_taken

    return HttpResponse(price)
