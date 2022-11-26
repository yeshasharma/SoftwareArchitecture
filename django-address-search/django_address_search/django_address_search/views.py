from django.shortcuts import render
from .models import AddressFormat, Country, Address
from django.http import HttpResponse


def country(request):
    data = []
    country_name = []
    country = request.POST.get('country_select')
    if country != None:
        countries = Country.objects.filter(name=country).values_list('cid', flat=True)
        names = Country.objects.filter(name=country)
        for name in names:
            print (name)
            country_name.append(name)
        for country_id in countries:
            posts = AddressFormat.objects.filter(cid=country_id)
            for formats in posts:
                data.append(str(formats).split(","))
        return render(request, 'addressFormat.html', {'format_list': data, 'country': country_name})
    else:
        countries = Country.objects.all()
        return render(request, 'index.html', {'countries': countries })


def address_elements(request):
    format_list = AddressFormat.objects.all()
    form_list = request.POST
    return render(request, 'index.html', {'format_list': format_list})


def search(request):
    data = []
    format_list = Address.objects.all()
    test = request.POST.getlist('elements')
    print("test>>>>>>>>>>>>>>>>>>>>>>>>>>>>", test)
    # if condition is for cross country search
    if test:
        Address.objects.filter(cid=test).values_list()
    country = request.POST.get('country_id')
    records = Country.objects.filter(name=country).values_list('cid', flat=True)
    for record in records:
        values = Address.objects.filter(cid=record).values_list()
        for value in values:
            data.append(str(value).split(","))
    return render(request, 'display.html', {'addresses': data})
