
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
    return HttpResponse(squirrel.Unique_squirrel_ID)


def squirrel_stats(request):
    sightings_stats1=Squirrel.objects.all().count()
    sightings_stats2=Squirrel.objects.filter(Primary_fur_color='Black').count()
    sightings_stats3=Squirrel.objects.filter(Primary_fur_color='Gray').count()
    sightings_stats4=Squirrel.objects.filter(Age='Adult').count()
    sightings_stats5=Squirrel.objects.filter(Age='Juvenile').count()
    context={'sightings_stats1':sightings_stats1,
            'sightings_stats2':sightings_stats2,
            'sightings_stats3':sightings_stats3,
            'sightings_stats3':sightings_stats3,
            'sightings_stats4':sightings_stats4,
            'sightings_stats5':sightings_stats5,
            }
    return render(request, 'sightings/stats.html', context)
