from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task, TaskDetail
from django.db.models import Q, Count

def dashboard(request):
    return render(request, "dashboard/manager_dashboard.html")

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
    form = TaskModelForm() # for GET

    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():

            form.save()
            # data = form.cleaned_data
            # title = data.get('title')
            # description = data.get('description')
            # due_date = data.get('due_date')
            # assigned_to = data.get('assigned_to')

            # task = Task.objects.create(title = title, descrition = description, due_date = due_date)
            # for emp_id in  assigned_to:
            #     employee = Employee.objects.get(id = emp_id)
            #     task.assigned_to.add(employee)

    context = {"form" : form}
    return render(request, "task_form.html", context)

    #retrive all data from tasks model
def view_task(request):
    # task = Task.objects.select_related('details').all()
    # tasks = TaskDetail.objects.select_related('task').all()
    # tasks = Task.objects.select_related('project').all() for foreign key 
    # tasks = Task.objects.select_related('project').all()  
    tasks = Task.objects.prefetch_related('assigned_to').all()  
    return render(request, "show_task.html", {"tasks": tasks})
