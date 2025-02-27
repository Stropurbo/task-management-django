from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm,TaskDetailModelForm
from tasks.models import Employee, Task, TaskDetail
from django.db.models import Q, Count
from django.contrib import messages

def dashboard(request):    
    # total_task = tasks.count()
    # completed_task = Task.objects.filter(status = 'COMPLETED').count()
    # task_in_progress = Task.objects.filter(status = 'IN_PROGRESS').count()
    # pending_task = Task.objects.filter(status = 'PENDING').count()

    # context = {
    #     'tasks' : tasks,
    #     "total_task" : total_task,
    #     "completed_task" : completed_task,
    #     "task_in_progress" : task_in_progress,
    #     "pending_task" : pending_task
    #     }

    type = request.GET.get('type', 'all')

    counts = Task.objects.aggregate(
        total = Count('id'),
        completed = Count('id', filter=Q(status = 'COMPLETED')),
        in_progress = Count('id', filter=Q(status = 'IN_PROGRESS')),
        pending = Count('id', filter=Q(status = 'PENDING')),
        )
    
    base_query = Task.objects.select_related('details').prefetch_related('assigned_to')

    if type == 'completed':
        tasks = base_query.filter(status = 'COMPLETED')
    elif type == 'in-progress':
        tasks = base_query.filter(status = 'IN_PROGRESS')
    elif type == 'pending':
        tasks = base_query.filter(status = 'PENDING')
    elif type == 'all':
        tasks = base_query.all()

    context = {
        "tasks" : tasks,
        "counts" : counts
    }

    return render(request, "dashboard/manager_dashboard.html", context)

    
def user_dashboard(request):
    return render(request, "dashboard/user_dashboard.html")

def test(request):
    context = {
        'name' : ['rakib', 'sakib', 'rocky'],
        'age' : 20
    }
    return render(request, 'test.html', context) 

def create_task(request):
    # em = Employee.objects.all()
    task_form = TaskModelForm() # for GET
    task_detail_form = TaskDetailModelForm()


    if request.method == 'POST':
        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetailModelForm(request.POST)
        
        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()  
            
            messages.success(request, "Task Created Successfully")
            return redirect('create-task')


    context = {"task_form" : task_form,'task_detail_form': task_detail_form}
    return render(request, "task_form.html", context)

    #retrive all data from tasks model

def update_task(request, id):
    task = Task.objects.get(id=id)
    task_form = TaskModelForm(instance=task)

    if task.details:
        task_detail_form = TaskDetailModelForm(instance=task.details)

    if request.method == 'POST':
        task_form = TaskModelForm(request.POST, instance=task)
        task_detail_form = TaskDetailModelForm(request.POST, instance = task.details)
        
        if task_form.is_valid() and task_detail_form.is_valid():
            
            task = task_form.save() 
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()            
           
            
            messages.success(request, "Task Updated Successfully")
            return redirect('update-task', id)


    context = {"task_form" : task_form,'task_detail_form': task_detail_form}
    return render(request, "task_form.html", context)

def delete_task(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        messages.success(request, "Task Deleted Successfully")
        return redirect('manager-dashboard')


#retrive all data from tasks model
def view_task(request):
    # task = Task.objects.select_related('details').all()
    # tasks = TaskDetail.objects.select_related('task').all()
    # tasks = Task.objects.select_related('project').all() for foreign key 
    # tasks = Task.objects.select_related('project').all()  
    tasks = Task.objects.prefetch_related('assigned_to').all()  
    return render(request, "show_task.html", {"tasks": tasks})
