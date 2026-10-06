from django import forms
from .models import Todo
class TodoForm(forms.Form):
    title = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Enter todo title", 'aria-label':"Todo Title", 'aria-describedby':"add-btn",}))
    detail = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control", 'placeholder':"Enter todo detail", 'aria-label':"Todo Detail", 'aria-describedby':"add-btn",}))
    complete = forms.BooleanField(required=False)
class ModelTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'detail', 'complete']
        widgets = {
        	'title': forms.TextInput(attrs={ 'class': 'form-control', 
            'placeholder': 'What do you need to do?', }), 
            'detail': forms.Textarea(attrs={ 'class': 'form-control', 'rows': 3, 
            'placeholder': 'Add some details (optional)...', }), 
        }