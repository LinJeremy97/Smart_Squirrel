from django.urls import path

from . import views

urlpatterns = [
        path('',views.all_squirrel),
        path('stats/',views.squirrel_stats),
        path('add/', views.add_sighting),
        path("<unique_id>/", views.edit_sighting),
    ]
