from django import forms
from tasks.models import Task, TaskDetail

# Django Form
class TaskForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    due_date = forms.DateField(widget=forms.SelectDateWidget, label='Due Date')
    assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[])

    def __init__(self, *args, **kwargs):
        em = kwargs.pop("em", []) 
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].choices = [
            (emp.id, emp.name) for emp in em
        ]

class StyleFormMixing:
    default_class = "border to-black shadow-sm focus:border-x-black focus:ring-black rounded-2xl w-full text-center "
    default_style = "border: 1px solid black; text-align: center; margin: 10px; width: 100%; padding: 10px"
    default_margin = "border: 1px solid black; margin:10px"

    def applyStyleWidget(self):
        for key, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class' : self.default_class,
                    'placeholder' : f"Enter {field.label.lower()}",
                    'style': self.default_style
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class' : self.default_class,
                    'placeholder' : f"Enter {field.label.lower()}",
                    'style': self.default_style
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    'class' : self.default_class,
                    'placeholder' : f"Enter {field.label.lower()}",
                    'style': self.default_margin
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'placeholder' : f"Enter {field.label.lower()}",
                    # 'style': self.default_margin
                })

# Django Model Form
class TaskModelForm(StyleFormMixing,forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','descrition','due_date','assigned_to']
        # exclude = ['project', 'is_completed', 'created_at', 'update_at'] #exclude mane bad deya
        labels = {
            'title': 'Title',
            'descrition': 'Description',
            'due_date': 'Due Date',
            'assigned_to': 'Employees',
        }
        widgets = {
            'due_date' : forms.SelectDateWidget,
            'assigned_to' : forms.CheckboxSelectMultiple
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.applyStyleWidget()
        
class TaskDetailModelForm(StyleFormMixing, forms.ModelForm):
    class Meta:
        model = TaskDetail
        fields = ['priority', 'notes']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.applyStyleWidget()