from django.shortcuts import render, redirect
from .models import Note 
from .forms import TodoForm

    # Create your views here.


def AddTodo(request): 
    form =TodoForm(request.POST or None)
    if form.is_valid():
        todo = form.save(commit=False) #commit =False will not be saved to datbase directly it will be save to todo object (commonly used in overwriting or default values)
        todo.save()
        all_notes = Note.objects.all()
        return redirect('/', {'all_todo':all_notes})

    return render(request,'notes/add.html',{'form':form})


def EditTodo(request,todo_id):
    single_todo=Note.objects.get(pk=todo_id)
    form = TodoForm(instance=single_todo)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=single_todo)  
        if form.is_valid():
            form.save()
            all_notes = Note.objects.all()
            return redirect('/', {'all_todo':all_notes})

    return render(request,'notes/edit.html',{'form':form})
        


def show_todo(request):
    all_notes = Note.objects.all() #query set
    return render(request, 'notes/show_todo.html', {'all_todo':all_notes})

    
def Delete(request,todo_id):
   single_todo=Note.objects.get(pk=todo_id)
   single_todo.delete()
   all_notes = Note.objects.all()
   return  redirect('/', {'all_todo':all_notes})    