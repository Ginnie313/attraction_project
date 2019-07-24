from django.shortcuts import render
from django.http import HttpResponse
from attractions.models import Attraction
import csv
from attractions.forms import AttractionForm


def index(request):
    return HttpResponse("Hello, Disney World!")

def home(request):
    with open("DisneyWorldAttractions.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Attraction.objects.get_or_create(
                attraction_name=row[0],
                height_req=row[1],
                tags=row[2],
                fastpass=row[3],
                park=row[4],
                area=row[5],
                notes=row[6])
            # creates a tuple of the new object or
            # current object and a boolean of if it was created
    return render(request,'home.html')

def advanced_search(request):
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AttractionForm(request.POST)
        print("benchmark 1")
        # check whether it's valid:
        if form.is_valid():
            print("benchmark 2")
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data['attraction_name']
            s_results = Attraction.objects.filter(attraction_name=name)
            print(s_results)
            return render('results.html', {'Results':s_results})
    else:
        form = AttractionForm()
    return render(request, "advanced_search.html", {'form': form})

def about(request):
    return render(request, "about.html")

def results(request):
    return render(request, "results.html", {"Results":results})

def attraction(request, attraction_name):
    attraction = Attraction.objects.get(attraction_name=attraction_name)
    return render(request, "attraction.html", {"Attraction":attraction})

def magic_kingdom(request):
    attraction_list = Attraction.objects.filter(park="Magic Kingdom")
    return render(request, "magic_kingdom.html", {"Attractions": attraction_list})

def about_mk(request):
    return render(request, "about_mk.html")

def epcot(request):
    attraction_list = Attraction.objects.filter(park="Epcot")
    return render(request, "epcot.html", {"Attractions": attraction_list})

def about_ep(request):
    return render(request, "about_ep.html")

def hollywood_studios(request):
    attraction_list = Attraction.objects.filter(park="Hollywood Studios")
    return render(request, "hollywood_studios.html", {"Attractions": attraction_list})

def about_hs(request):
    return render(request, "about_hs.html")

def animal_kingdom(request):
    attraction_list = Attraction.objects.filter(park="Animal Kingdom")
    return render(request, "animal_kingdom.html", {"Attractions": attraction_list})

def about_ank(request):
    return render(request, "about_ank.html")
