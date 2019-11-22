from django.db import models

from django.utils.translation import gettext as _

# Create your models here.

class Squirrel(models.Model):
    Latitude = models.DecimalField(
            help_text=_("Latitude of squirrel"),
            max_digits=30,
            decimal_places=2,
     )
    Longitude = models.DecimalField(
            help_text=_("Longitude of squirrel"),
            max_digits=30,
            decimal_places=2,
    )
    Squirrel_ID = models.CharField(
            help_text=_("Unique squirrel id"),
            max_length=50,
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
            choices = SHIFT_CHOICES,
            max_length=10,
            default=AM,
    )
    Date = models.IntegerField(
            help_text=_("sighting session day and month"),
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
            choice=AGE_CHOICES,
            max_length=15,
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
            choice=PRIMARYFURCOLOR_CHOICES,
            max_length=20,

    )

    Highlight_fur_color = models.TextField(
            help_text=_("Highlight fur color of squirrel, if it has more than on color, please intersect with ','"),
            max_length=100,
    )

    Combination_color = models.TextField(
            help_text=_("Combination of fur color, please use'+'"),
            max_length=100,
    )

    Color_notes = models.TextField(
            help_text=_("Color notes of squirrel"),
            max_length=150,
    )

    GroundPlane = 'Ground Plane'
    AboveGround = 'Above Ground'


    LOCATION_CHOICES = (
            (GroundPlane,'Ground Plane'),
            (AboveGround,'Above Ground'),
    )
    Location = models.CharField(
            help_text=_("location of squirrel"),
            choice=LOCATION_CHOICES,
            max_length=20,
    )
    
    Above_Measure = models.TextField(
            help_text=_("Above Ground Sighter Measurement"),
            max_length=20,
    )

    Specific_location =  models.TextFiled(
            help_text=_("Specific location of squirrel"),
            max_length=100,
    )

    Running = models.BooleanField(
            help_text=_("run or not?"),
    )

    Chasing = models.BooleanField(
            help_text=_("chase or not?"),
    )

    Climbing = models.BooleanField(
            help_text=_("Climb or not?"),
    )

    Eating = models.BooleanField(
            help_text=_("Eat or not?"),
    )

    Foraging = models.BooleanField(
            help_text=_("Forage or not?"),
    )

    Other_Activities =  models.TextField(
            help_text=_("Other Activities of squirrel"),
            max_length=150,
    )

    Kuks = models.BooleanField(
            help_text=_("Kuks or not?"),
    )

    Quaas = models.BooleanField(
            help_text=_("Quaas or not?"),
    )

    Moans = models.BooleanField(
            help_text=_("Moans or not?"),
    )

    Tail_flags = models.BooleanField(
            help_text=_("Tail flags or not?"),
    )

    Tail_twitches = models.BooleanField(
            help_text=_("Tail twitches or not?"),
    )

    Approaches = models.BooleanField(
            help_text=_("Approaches or not?"),
    )

    Indifferent = models.BooleanField(
            help_text=_("Indifferent or not?"),
    )

    Runs_from = models.BooleanField(
            help_text=_("Runs from or not?"),
    )

    def __str__(self):
        return self.Squirrel_ID
