from django.shortcuts import render, HttpResponse

# Create your views here.
def showTripsView(request):
    return render(request, 'travelsites/showtrips.html')

def showAfricaPageView(request):
    context = {
        'area': 'Africa'
    }
    return render(request, 'travelsites/displaytrip.html', context)

def showAustraliaPageView(request):
    context = {
        'area': 'Africa'
    }
    return render(request, 'travelsites/displaytrip.html', context)

def showAsiaPageView(request):
    context = {
        'area': 'Asia'
    }
    return render(request, 'travelsites/displaytrip.html', context)

def showEuropePageView(request):
    context = {
        'area': 'Europe'
    }
    return render(request, 'travelsites/displaytrip.html', context)

def showNorthAmericaPageView(request):
    context = {
        'area': 'North America'
    }
    return render(request, 'travelsites/displaytrip.html', context)

def showSouthAmericaPageView(request):
    context = {
        'area': 'South America' 
    }
    return render(request, 'travelsites/displaytrip.html', context)

