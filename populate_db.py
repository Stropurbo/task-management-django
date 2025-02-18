import os
import django
from faker import Faker
import random
from tasks.models import Employee, Task, Project, TaskDetail

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management.settings')
django.setup()

def populate_db():
    fake = Faker()

    # create project
    projects = [Project.objects.create(
        name = fake.bs().capitalize(),
        description = fake.paragraph(),
        start_date = fake.date_this_year()
    ) for _ in range(5)]
    print(f'Created {len(projects)} projects.')

    # create employee
    employees = [Employee.objects.create(
        name = fake.name(),
        email = fake.email()
    ) for _ in range(10) ]
    print(f'Created {len(employees)} employees.')

    # create Task

    tasks = []
    for _ in range(20):
        task = Task.objects.create(
            project = random.choice(projects),
            title = fake.sentence(),
            descrition = fake.paragraph(),
            due_date = fake.date_this_year(),
            status = random.choice(['PENDING', 'IN_PROGRESS', 'COMPLETED']),
            is_completed = random.choice([True, False])
        )
        task.assigned_to.set(random.sample(employees, random.randint(1,3)))
        tasks.append(task)
    print(f'created {len(tasks)} tasks.')

    # Created for task details

    for task in tasks:
        TaskDetail.objects.create(
            task = task,
            assigned_to = ", ".join(
                [emp.name for emp in task.assigned_to.all()]),
                priority = random.choice(['H', 'M', 'L']),
                notes = fake.paragraph()
        )
    print("Populated TaskDetails for all tasks.")
    print("Database populated successfully!")