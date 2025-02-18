from django.db import models
class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(auto_now=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed')
    ]

    project = models.ForeignKey(Project,
    on_delete=models.CASCADE, 
    default=1,
    )
    
    title = models.CharField(max_length=250)
    descrition = models.TextField()
    due_date = models.DateField()
    assigned_to = models.ManyToManyField(Employee)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='PENDING')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TaskDetail(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'

    PRIORITY_OPTIONS = (
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low')
    )
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    assigned_to = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default= LOW)
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Details form Task{self.task.title}"
