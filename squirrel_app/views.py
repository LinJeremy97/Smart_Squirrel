# Create your views here.
from sightings.models import Squirrel 
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def detail(request):
    sightings=Squirrel.objects.all()
    context={
        'sightings':sightings,
    }
    return render(request, 'squirrel_app/squirrel_app.html',context)
