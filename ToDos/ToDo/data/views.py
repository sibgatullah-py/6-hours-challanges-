from django.shortcuts import render, redirect, get_object_or_404
from .models import Data
from .forms import DataForm

def index(request):
    data = Data.objects.all().order_by('id')
    return render(request, 'data/index.html', {'data':data})

def add_task(request):
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

def edit_task(request, task_id):
    data = get_object_or_404(Data, pk=task_id )
    if request.method == "POST":
        form = DataForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('index')
    else:
        form = DataForm(instance=data)
    return render(request, 'data/data_form.html', {'form':form})


def delete_task(request, task_id):
    data  = get_object_or_404(Data, pk=task_id,)
    if request.method=="POST":
        data.delete()
        return redirect('index')
    
    return render(request, 'data/index.html')