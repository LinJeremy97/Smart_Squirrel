from django.urls import path

from . import views

urlpatterns = [
        path(<'<int:squirrel_id>/',views.squirrel_details),
    ]
