from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'project/home.html')

def password(request):
    thepassword = ''
    characters = list('qwertyuiopasdfghjklzxcvbnm')
    length = int(request.GET.get('Len', 9))

    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    if request.GET.get('numbers'):
        characters.extend(list('123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))

    for _ in range(length):
        thepassword += random.choice(characters)
    return render(request, 'project/password.html', {'password':thepassword} )

def description(request):
    return render(request,'project/description.html')
# Create your views here.
