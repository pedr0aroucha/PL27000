from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


@login_required(login_url='/login')
def create_view(request):
    form = TaskForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('/task/list')
        else:
            return redirect('/task/create')
    return render(request, "create.html")


@login_required(login_url='/login')
def read_view(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "list.html", {"task_list": tasks})


@login_required(login_url='/login')
def update_view(request, pk):
    form = TaskForm()
    task = Task.objects.get(id=pk)
    if request.POST:
        task.name = request.POST.get('name')
        task.description = request.POST.get('description')
        task.lastday = request.POST.get('lastday')
        if request.POST.get('taskok') == 'on':
            task.taskok = True
        else:
            task.taskok = False
        task.user = request.user

        task.save()
        return redirect("/task/list/")
        # else:
        #     pass
    return render(request, "update.html", {"task": task, "form": form})


@login_required(login_url='/login')
def delete_view(request, pk):
    task = Task.objects.get(id=pk)
    if request.POST:
        task.delete()
        return redirect('/task/list')
    return render(request, "delete.html", {"task": task})
