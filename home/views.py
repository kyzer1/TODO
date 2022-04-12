from django.shortcuts import redirect, render
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm, TodoUpdateForm


def home(request):
    qs = Todo.objects.all()
    context = {
        'todos': qs
    }
    return render(request, 'home.html', context)


def detail(request, id):
    todo = Todo.objects.get(id=id)
    return render(request, 'detail.html', context={'todo': todo})


def delete(request, id):
    delete_object = Todo.objects.get(id=id).delete()
    messages.success(request, 'todo deleted successfuly', 'success')
    return redirect('home')


def create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'], body=cd['body'], created=cd['created'])
            messages.success(request, 'todo created successfuly', 'success')
            return redirect('home')
    else:
        form = TodoCreateForm()
    return render(request, 'create.html', {'form': form})


def update(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid:
            form.save()
            messages.success(request, 'your todo updated successfuly', 'success')
            return redirect('details', id)   
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request, 'update.html', {'form': form})
    


