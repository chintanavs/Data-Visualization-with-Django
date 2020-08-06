from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers # to translate data to other format

#importing dashboard model
from dashboard.models import Order


# Create your views here.

def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})


def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False) # safe=False so that any type of data can be passed, if True only dict can be passed
