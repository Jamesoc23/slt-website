## Get the path function which is used to deal with the url patterns
from django.urls import path


## Get the functions in the views  
from . import views

## Set the url patterns to route the views
urlpatterns = [
    ## path(route, view, name)
    path('', views.index, name='index'),
]