from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoItems


def todoview(request):
    all_to_item = TodoItems.objects.all()
    return render(request, 'todo.html', {'all_items': all_to_item})


def addTodo(request):
    new_item = TodoItems(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')


def deleteTodo(request, todo_id):
    item_to_delete = TodoItems.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
