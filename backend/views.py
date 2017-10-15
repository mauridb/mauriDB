from django.shortcuts import render


# application routing
def home(request):
    context = {
        'msg': 'django html'
    }
    return render(request, 'home.html', context)


def login(request):
    context = {
        'msg': 'login html'
    }
    return render(request, 'login.html', context)


def registration(request):
    context = {
        'msg': 'registration html'
    }
    return render(request, 'registration.html', context)


def dashboard(request):
    context = {
        'msg': 'dashboard html'
    }
    return render(request, 'dashboard.html', context)


# design APIrest with djangorestframework here..
