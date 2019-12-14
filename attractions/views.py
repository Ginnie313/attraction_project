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
    if 'search' in request.GET:
        name =  request.GET.get('search')
        try:
            #Here the icontains gets any attraction with the text in the name
            attraction_list = Attraction.objects.filter(attraction_name__icontains=name)
            print(attraction)
            #working okay up to here.need to add ability to search for part of name?
            return render(request,"results.html",{"Results":attraction_list})
        except:
            print("Some sort of error occured")
            return render(request, 'home.html')
    return render(request,'home.html')

def advanced_search(request):
    #top nav search bar
    if 'search' in request.GET:
        name =  request.GET.get('search')
        try:
            #Here the icontains gets any attraction with the text in the name
            attraction_list = Attraction.objects.filter(attraction_name__icontains=name)
            print(attraction)
            #working okay up to here.need to add ability to search for part of name?
            return render(request,"results.html",{"Results":attraction_list})
        except:
            print("Some sort of error occured")
            return render(request, 'advanced_search.html')
    #note: just kinda randomly stopped working then started again?
    #Did the user ask for a name?
    if 'q1' in request.GET:
        name = request.GET.get('q1')
        print(name)
    #Did the user ask for a height requirement?
    if 'q2' in request.GET:
        height = request.GET.get('q2')
        print(height)
    #Note, search for tags is currently only working for one tag at a time and you MUST choose a tag
    #need to find implementation of default "" tag?
    if 'q3' in request.GET:
        tags = request.GET.get('q3')
        print(tags)
    try:
        #Return the list of attractions that meet all parameters
        attraction_list = Attraction.objects.filter(attraction_name__icontains=name, height_req__icontains=height, tags__icontains=tags)
        return render(request,"results.html",{"Results":attraction_list})
    except:
        print("Some sort of error occured")
        return render(request, 'advanced_search.html')

    return render(request, "advanced_search.html")

def about(request):
    if 'search' in request.GET:
        name =  request.GET.get('search')
        try:
            #Here the icontains gets any attraction with the text in the name
            attraction_list = Attraction.objects.filter(attraction_name__icontains=name)
            print(attraction)
            return render(request,"results.html",{"Results":attraction_list})
        except:
            print("Some sort of error occured")
            return render(request, 'home.html')
    return render(request, "about.html")

def results(request):
    if 'search' in request.GET:
        name =  request.GET.get('search')
        try:
            #Here the icontains gets any attraction with the text in the name
            attraction_list = Attraction.objects.filter(attraction_name__icontains=name)
            print(attraction)
            #working okay up to here.need to add ability to search for part of name?
            return render(request,"results.html",{"Results":attraction_list})
        except:
            print("Some sort of error occured")
            return render(request, 'home.html')
    return render(request, "results.html", {"Results":results})

def attraction(request, attraction_name):
    if 'search' in request.GET:
        name =  request.GET.get('search')
        try:
            #Here the icontains gets any attraction with the text in the name
            attraction_list = Attraction.objects.filter(attraction_name__icontains=name)
            print(attraction)
            #working okay up to here.need to add ability to search for part of name?
            return render(request,"results.html",{"Results":attraction_list})
        except:
            print("Some sort of error occured")
            return render(request, 'home.html')
    attraction = Attraction.objects.get(attraction_name=attraction_name)
    return render(request, "attraction.html", {"Attraction":attraction})

def magic_kingdom(request):
    if 'search' in request.GET:
        name =  request.GET.get('search')
        try:
            #Here the icontains gets any attraction with the text in the name
            attraction_list = Attraction.objects.filter(attraction_name__icontains=name)
            print(attraction)
            #working okay up to here.need to add ability to search for part of name?
            return render(request,"results.html",{"Results":attraction_list})
        except:
            print("Some sort of error occured")
            return render(request, 'home.html')
    attraction_list = Attraction.objects.filter(park="Magic Kingdom")
    return render(request, "magic_kingdom.html", {"Attractions": attraction_list})

def about_mk(request):
    if 'search' in request.GET:
        name =  request.GET.get('search')
        try:
            #Here the icontains gets any attraction with the text in the name
            attraction_list = Attraction.objects.filter(attraction_name__icontains=name)
            print(attraction)
            #working okay up to here.need to add ability to search for part of name?
            return render(request,"results.html",{"Results":attraction_list})
        except:
            print("Some sort of error occured")
            return render(request, 'home.html')
    return render(request, "about_mk.html")

def epcot(request):
    if 'search' in request.GET:
        name =  request.GET.get('search')
        try:
            #Here the icontains gets any attraction with the text in the name
            attraction_list = Attraction.objects.filter(attraction_name__icontains=name)
            print(attraction)
            #working okay up to here.need to add ability to search for part of name?
            return render(request,"results.html",{"Results":attraction_list})
        except:
            print("Some sort of error occured")
            return render(request, 'home.html')
    attraction_list = Attraction.objects.filter(park="Epcot")
    return render(request, "epcot.html", {"Attractions": attraction_list})

def about_ep(request):
    if 'search' in request.GET:
        name =  request.GET.get('search')
        try:
            #Here the icontains gets any attraction with the text in the name
            attraction_list = Attraction.objects.filter(attraction_name__icontains=name)
            print(attraction)
            #working okay up to here.need to add ability to search for part of name?
            return render(request,"results.html",{"Results":attraction_list})
        except:
            print("Some sort of error occured")
            return render(request, 'home.html')
    return render(request, "about_ep.html")

def hollywood_studios(request):
    if 'search' in request.GET:
        name =  request.GET.get('search')
        try:
            #Here the icontains gets any attraction with the text in the name
            attraction_list = Attraction.objects.filter(attraction_name__icontains=name)
            print(attraction)
            #working okay up to here.need to add ability to search for part of name?
            return render(request,"results.html",{"Results":attraction_list})
        except:
            print("Some sort of error occured")
            return render(request, 'home.html')
    attraction_list = Attraction.objects.filter(park="Hollywood Studios")
    return render(request, "hollywood_studios.html", {"Attractions": attraction_list})

def about_hs(request):
    if 'search' in request.GET:
        name =  request.GET.get('search')
        try:
            #Here the icontains gets any attraction with the text in the name
            attraction_list = Attraction.objects.filter(attraction_name__icontains=name)
            print(attraction)
            #working okay up to here.need to add ability to search for part of name?
            return render(request,"results.html",{"Results":attraction_list})
        except:
            print("Some sort of error occured")
            return render(request, 'home.html')
    return render(request, "about_hs.html")

def animal_kingdom(request):
    if 'search' in request.GET:
        name =  request.GET.get('search')
        try:
            #Here the icontains gets any attraction with the text in the name
            attraction_list = Attraction.objects.filter(attraction_name__icontains=name)
            print(attraction)
            #working okay up to here.need to add ability to search for part of name?
            return render(request,"results.html",{"Results":attraction_list})
        except:
            print("Some sort of error occured")
            return render(request, 'home.html')
    attraction_list = Attraction.objects.filter(park="Animal Kingdom")
    return render(request, "animal_kingdom.html", {"Attractions": attraction_list})

def about_ank(request):
    if 'search' in request.GET:
        name =  request.GET.get('search')
        try:
            #Here the icontains gets any attraction with the text in the name
            attraction_list = Attraction.objects.filter(attraction_name__icontains=name)
            print(attraction)
            #working okay up to here.need to add ability to search for part of name?
            return render(request,"results.html",{"Results":attraction_list})
        except:
            print("Some sort of error occured")
            return render(request, 'home.html')
    return render(request, "about_ank.html")
