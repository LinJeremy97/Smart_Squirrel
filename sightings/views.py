
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Squirrel
def squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels':squirrels,
            }
    return render(request,'sightings/all.html',context)
def squirrels_details(request,squirrel_id):
    squirrel = Squirrel.objects.get(id=squirrel_id)
    return HttpResponse(squirrel.Squirrel_ID)
