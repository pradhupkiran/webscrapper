import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Links


# Create your views here.
def home(request):
    if request.method=='POST':
        new_link=request.POST.get('page','')
        url = requests.get(new_link)
        bs = BeautifulSoup(url.text, 'html.parser')
        # print(bs.prettify())
        # bs.findAll('b')

        for link in bs.findAll('a'):
            li_add = link.get('href')
            li_name = link.string
            Links.objects.create(address=li_add, string_name=li_name)
        return HttpResponseRedirect('/')

    else:
        data_values = Links.objects.all()

    return render(request, 'home.html', {'data_values': data_values})
