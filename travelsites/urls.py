from django.contrib import admin
from django.urls import path
from .views import showTripsView, showAfricaPageView, showAsiaPageView, showAustraliaPageView, showEuropePageView, showNorthAmericaPageView, showSouthAmericaPageView

urlpatterns = [
    path('', showTripsView, name='showtrips'),
    path('africa/', showAfricaPageView, name='africa'),
    path('australia/', showAustraliaPageView, name='australia'),
    path('asia/', showAsiaPageView, name='asia'),
    path('europe/', showEuropePageView, name='europe'),
    path('northamerica/', showNorthAmericaPageView, name='northamerica'),
    path('southamerica/', showSouthAmericaPageView, name='southamerica'),
]