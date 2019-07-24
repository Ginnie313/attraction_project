from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('magic_kingdom', views.magic_kingdom),
    path('epcot', views.epcot),
    path('hollywood_studios', views.hollywood_studios),
    path('animal_kingdom', views.animal_kingdom)
]
