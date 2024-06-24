from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .Algorithm import  search_algorithm
# Create your views here.



def index(response):
    data=""
    if response.method=="POST":
        # search_form=response.POST
        data = search_algorithm(response.POST.getlist("start"),response.POST.getlist("goal"))
    else:
        search_fields=''
    return render(response,'main/index.html', {"data":data})
