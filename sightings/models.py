from django.db import models 
from django.utils.translation import gettext as _

class Squirrel(models.Model): 
    Latitude= models.DecimalField( 
            help_text=_("Latitude of squirrel"), 
            max_digits=30, 
            decimal_places=20, 
            ) 
    Longitude = models.DecimalField(
            help_text=_("Longitude of squirrel"), 
            max_digits=30, 
            decimal_places=20, 
            ) 
    Unique_squirrel_ID = models.CharField(
            help_text=_("Unique squirrel id"),
            max_length=50,
            primary_key=True,
            )
    Hectare = models.CharField(
            help_text=_("Hectare of squirrel,like 32D"),
            max_length=10,
            )
    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = (
            (AM,'AM'),
            (PM,'PM'),
            )
    Shift = models.CharField(
            help_text=_("Shift of squirrel"),
            choices=SHIFT_CHOICES,
            max_length=15,
            default=AM,
            )
    Date = models.DateField(
             help_text=_('Date'),
             null=True,
             )
    Hectare_squirrel_num = models.SmallIntegerField(
            help_text=_("number within the chronological sequence of squirrel sightings"), 
            ) 
    Adult = 'Adult' 
    Juvenile = 'Juvenile' 
    AGE_CHOICES = (
            (Adult,'Adult'),
            (Juvenile,'Juvenile'), 
            ) 
    Age = models.CharField( 
            help_text=_("Age of squirrel"), 
            choices=AGE_CHOICES, 
            max_length=15, 
            default=False,
            )
    Gray = 'Gray' 
    Black = 'Black' 
    Cinnamon = 'Cinnamon' 
    PRIMARYFURCOLOR_CHOICES = ( 
            (Gray,'Gray'),
            (Black,'Black'),
            (Cinnamon,'Cinnamon'), 
            )
    Primary_fur_color = models.CharField(
            help_text=_("Primary fur color of squirrel"),
            choices=PRIMARYFURCOLOR_CHOICES, 
            max_length=20,
            default=False,
            ) 
    GroundPlane = 'Ground Plane' 
    AboveGround = 'Above Ground' 
    LOCATION_CHOICES = ( 
            (GroundPlane,'Ground Plane'), 
            (AboveGround,'Above Ground'), 
            ) 
    Location = models.CharField( 
            help_text=_("location of squirrel"), 
            choices=LOCATION_CHOICES, 
            max_length=20,
            default=False,
            )  
             
    Specific_location = models.CharField( 
            help_text=_("Specific location of squirrel"), 
            max_length=100, 
            default=False,
            )
    TRUE='TRUE'
    FALSE='FALSE'
    Running = models.CharField(help_text=_('Running'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Chasing = models.CharField(help_text=_('Chasing'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Climbing = models.CharField(help_text=_('Climbing'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Eating = models.CharField(help_text=_('Eating'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Foraging = models.CharField(help_text=_('Foraging'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    


    Other_Activities = models.CharField( 
            help_text=_("Does squirrel have other activities?"), 
            max_length=100,
            null=True,
            blank=True,
            )

    Kuks = models.CharField(help_text=_('Kuks'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Quaas = models.CharField(help_text=_('Quaas'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Moans = models.CharField(help_text=_('Moans'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Tail_Flags = models.CharField(help_text=_('Tail flags'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Tail_Twitches = models.CharField(help_text=_('Tail twitches'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Approaches = models.CharField(help_text=_('Approaches'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Indifferent = models.CharField(help_text=_('Indifferent'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)
    Runs_From = models.CharField(help_text=_('Runs from'),
            choices=((TRUE,'TRUE'),(FALSE,'FALSE')),default=FALSE,max_length=5,null=True)

    def __str__(self): 
        return self.Unique_squirrel_ID 
    def get_absolute_url(self):
        return reverse('', kwargs={'id':self.Unique_squirrel_ID})
# Create your models here.

