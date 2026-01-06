# task_main/views.py
from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from task_main.models import Task

def home(request):
    if request.method == "POST":
        task_text = request.POST.get("task")
        if task_text:
            Task.objects.create(task=task_text)

    tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)

    return render(request, "home.html", {
        "tasks": tasks,
        "completed_tasks": completed_tasks,
    })


def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = True
    task.save()
    return redirect("home")


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("home")


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.task = request.POST.get("task")
        task.save()
        return redirect("home")

    return render(request, "edit_task.html", {"task": task})
