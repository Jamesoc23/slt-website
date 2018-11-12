from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Service, ContactInfo, About


def index(request):

    service = Service.objects.all()
    about = About.objects.first()
    contactInfo = ContactInfo.objects.first()

    context = {
        'services': service,
        'contactInfo': contactInfo,
        'about': about,
    }
    return render(request, 'sltapp/index.html', context)


