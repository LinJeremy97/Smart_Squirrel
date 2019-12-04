from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import requests, csv, re, sys
from dateutil import parser
from datetime import date

class Command(BaseCommand):
    help ='Export squirrel data from NYC Central Park'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='path of file to be exported')

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        
        with open(path, mode='wb') as csvfile:
            writer = csv.writer(csvfile)
            squirrels = Squirrel.objects.all()
            writer.writerow['X','Y','Unique Squirrel ID','Hectare',
                    'Shift','Date','Hectare Squirrel Number','Age','Primary Fur Color','Highlight Fur Color','Combination of Primary and Highlight Color','Color Notes','Location','Specific Location','Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from']

                        

            for squirrel in squirrels:
                    writer.writerow([
                    squirrel.Latitude,Longitude,
                    squirrel.Unique_Squirrel_ID,
                    squirrel.Hectare,
                    squirrel.Shift,
                    squirrel.Date ,
                    squirrel.Hectare_Squirrel_Number ,
                    squirrel.Age ,
                    squirrel.Primary_Fur_Color ,
                    squirrel.Location ,
                    squirrel.Specific_Location ,
                    squirrel.Running ,
                    squirrel.Chasing ,
                    squirrel.Climbing ,
                    squirrel.Eating ,
                    squirrel.Foraging ,
                    squirrel.Other_Activities ,
                    squirrel.Kuks ,
                    squirrel.Quaas ,
                    squirrel.Moans ,
                    squirrel.Tail_Flags ,
                    squirrel.Tail_Twitches ,
                    squirrel.Approaches ,
                    squirrel.squirrel.Indifferent ,
                    squirrel.Runs_From ,
                ])
        csvfile.close() 
