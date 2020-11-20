from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
	#return HttpResponse("my_to_do_app first padge")
        return render(request, 'my_to_do_app/index.html')
