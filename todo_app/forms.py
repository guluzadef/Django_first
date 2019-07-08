from django import forms
from .models import TodoModel

class TodoForm(forms.ModelForm):

    class Meta:
        model= TodoModel
        fields=[
            "title","description"
        ]
        widgets={
            "title":forms.TextInput(attrs={
                "class":"form-control"
            }),
            "description":forms.Textarea(attrs={
                "class":"form-control"
            })
        }