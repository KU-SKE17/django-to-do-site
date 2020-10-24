import datetime
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    """Form for inputing a new todo item.
    The done field is not shown, since it's useless to add a todo that
    is already done.
    """    
    class Meta:
        model = Todo
        fields = ['description'] # don't show 'done' field on form for a new todo
        # this doesn't work
        hidden = ['id']
        # custom labels for input fields
        labels = {
            'description': "Description of todo",
            'done': "Is it Done?",
        }

    
    def clean_description(self):
        """Verify the description has required minimum length"""
        description = self.cleaned_data['description']
        if len(description.strip()) < 3:
            raise forms.ValidationError("Description should be at least 3 chars")
        # returned value replaces cleaned data
        return description
