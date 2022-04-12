from dataclasses import field
from pyexpat import model
from django import forms
from .models import Todo

class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'body', 'created')