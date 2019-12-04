from django.urls import path

from . import views

urlpatterns = [
        path('',views.squirrels_details),
        path('stats/',views.squirrel_stats),
    ]
