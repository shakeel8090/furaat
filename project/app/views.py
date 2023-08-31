from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name':'FURAAT'})


def add(request):
    val1 = int(request.GET.get('num1'))
    val2 = int(request.GET.get('num2'))
    res = val1 + val2
    return render(request, 'results.html', {'results':res})