from django.shortcuts import render
from .models import Data

def index(request):
    data = Data.objects.all().order_by('id')
    return render(request, 'data/index.html', {'data':data})
