from django.contrib import admin
from django.urls import path,include
from .import views
#from empmodule.views import view_jobdetails

app_name='empmodule'
urlpatterns = [
    path('jobpost/',views.jobpost,name='jobpost'),
    path('add_jobdetails',views.add_jobdetails,name='add_jobdetails'),
    path('view/',views.view_jobdetails,name='view_jobdetails'),
    path('feedback/',views.feedback,name='feedback')
]