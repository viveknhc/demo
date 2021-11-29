from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dmfn(request):
    return HttpResponse("good day")
def fnsample(req):
    return render(req,"sample.html")    
