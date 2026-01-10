from django.shortcuts import render, redirect
from .models import Data
from .forms import DataForm

def index(request):
    data = Data.objects.all().order_by('id')
    return render(request, 'data/index.html', {'data':data})

def add_task(request):
    data = None
    if request.method == "POST":
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('index')
    else:
        form = DataForm()
        
        
    return render(request, 'data/data_form.html', {'form':form})
