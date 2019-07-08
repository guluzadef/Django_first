from django.shortcuts import render,redirect

from todo_app.forms import TodoForm
from .forms import TodoForm,TodoModel
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.
def home_page(request):
    context={}
    if "search" in  request.GET:
        query=request.GET.get("search")
        context["todo_list"]=TodoModel.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
    else:


        context["todo_list"]=TodoModel.objects.all().order_by("-id")
    return render(request,"todo.html",context)



def create_todo(request):
    if request.method=="POST":
        data=request.POST
        form=TodoForm(data)
        if form.is_valid():#eger form duzgundurse
            form.save()
            return redirect("home")
        else:#form yanlishdirsa
            context = {}
            context["form"] = form
            return render(request, "todo_form.html", context)

    else:
        context={}
        context["form"]=TodoForm
        return render(request,"todo_form.html",context)


def update_view(request,id):
    todo=TodoModel.objects.filter(id=id).last()
    if request.method=="GET":
        if todo:
            form=TodoForm(instance=todo)
            context={}
            context["form"]=form
            return render(request,"todo_form.html",context)

        else:
            return HttpResponse("Bele bir object yoxdur!")

    else:
        form=TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            context={}
            context["form"]=form
            return render(request,"todo_form.html",context)


def delete_view(request,id):
    todo=TodoModel.objects.filter(id=id).last()
    if request.method=="GET":
        context={}
        context["todo"]=todo
        return render(request,"delete_todo.html",context)
    else:
        todo.delete()
        return redirect("home")

def show_view(request,id):
    todo=TodoModel.objects.filter(id=id).last()
    context={}
    context["todo"]=todo
    return render(request,"show_todo.html",context)

def search_view(request,ind):
    pass