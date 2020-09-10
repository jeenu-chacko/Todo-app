from django import forms
from .models import Note

class TodoForm(forms.ModelForm):

    class Meta:
        model = Note
        # fields = '__all__'
        fields = ('title','desc','deadline','completed')
        
        
