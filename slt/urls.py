## Get the path function which is used to deal with the url patterns
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


## Get the functions in the views  
from . import views

## Set the url patterns to route the views
urlpatterns = [
    ## path(route, view, name)
    path('', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)