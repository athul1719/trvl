from django.http import  HttpResponse
from django.shortcuts import render
from .models import place
from .models import names
# Create your views here.
def demo(request):
    obj=place.objects.all()
    nam=names.objects.all()
    return render(request,'index.html',{'result':obj,'result1':nam})

# def about(request):
#     return render(request,'about.html')