from django.shortcuts import render
from django.http import HttpResponse


def home(request): #return what we want the user to see when they land here, handles homepage traffic
	return render(request, 'liveScore/home.html')

def about(request):
	return HttpResponse('<h1>About</h1>')



# Create your views here.


