from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Webpage
from AppTwo.models import AccessRecord
# Create your views here.

def index(request):
    return HttpResponse('<em> My Second App </em>')

def help_view(request):
    return render(request,'help.html')

def webpage_view(request):
    webpages = Webpage.objects.all()
    access_records = AccessRecord.objects.all()
    return render(request, 'webpage.html', {'webpages': webpages, 'access_records': access_records})