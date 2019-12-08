
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Squirrel
from .forms import SightingForm

def squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels':squirrels,
            }
    return render(request,'sightings/all.html',context)


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


def edit_sighting(request, unique_id):
    sighting = Squirrel.objects.get(Unique_squirrel_ID=unique_id)
    if request.method == 'POST':
        form = SightingForm(request.POST, instance=sighting)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SightingForm(instance=sighting)

    context = {
            'form': form,
    }

    return render(request, 'sightings/edit.html', context)


def add_sighting(request):
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SightingForm()

    context = {
            'form': form,
    }

    return render(request, 'sightings/add.html', context)


def all_squirrel(request):
    if request.method == "GET":

        sightings = Squirrel.objects.all()
        context = {
                'sightings': sightings,
        }
        return render(request,'sightings/all.html', context)



