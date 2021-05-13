from django.shortcuts import render 
from .models import Reporting

def index(request):
    rep = Reporting.objects.all() 
    context = {'rep': rep} 
    return render(request, 'reports/baser.html', context)

