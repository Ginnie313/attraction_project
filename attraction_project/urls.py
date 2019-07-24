"""attraction_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from attractions import views

urlpatterns = [
    path('attractions/', include('attractions.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('magic_kingdom', views.magic_kingdom),
    path('epcot', views.epcot),
    path('hollywood_studios', views.hollywood_studios),
    path('animal_kingdom', views.animal_kingdom),
    path('advanced_search', views.advanced_search),
    path('attraction/<str:attraction_name>',views.attraction),
    path('about/', views.about),
    path('about_mk/',views.about_mk),
    path("about_ep/",views.about_ep),
    path("about_hs/",views.about_hs),
    path("about_ank/",views.about_ank),
    path("results/",views.results)
]
