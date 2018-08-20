from django.shortcuts import render
from .models import  dummy_table
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index (request):

    locations = dummy_table.objects.order_by('lat').values('lat', 'lng').distinct()

    tdata = dummy_table.objects.order_by('-dtordinal')

    context ={'tdata': tdata, 'locations':locations}

    return render(request, 'test.html', context)

