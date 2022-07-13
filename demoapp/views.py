from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskDb

# Add Blog

def home(request):
    # employees = TaskDb.objects.all()  
    
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                pass
    else:
        form = TaskForm()


    # return render(request, 'index.html', {'form':form,'employees':employees})
    return render(request, 'index.html', {'form':form})


def update(request, id):  
    employee = TaskDb.objects.get(id=id)  
    form = TaskForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("home")  
    return render(request, 'edit.html', {'form':form,'employee':employee})


def destroy(request, id):  
    employee = TaskDb.objects.get(id=id)  
    employee.delete()  
    return redirect("home")  