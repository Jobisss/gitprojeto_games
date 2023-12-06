from django.shortcuts import render


def inicio(request):
    return render(request, 'index.html')

def animal1(request):
    return render (request, 'cacau.html')

def animal2(request):
    return render (request, 'duke.html')

def animal3(request):
    return render (request, "luiza.html")

