
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Customer, Product, Todo
from django.shortcuts import render, get_object_or_404
# from django.contrib.auth import logout

# Create your views here.



def reg(request):
    if request.method== 'POST':
        f_name= request.POST['first_name']
        l_name= request.POST['last_name']
        u_name= request.POST['username']
        u_pass= request.POST['password']
        f_pass= request.POST['confirm_password']
        if u_name and u_pass and f_pass !='':

            if u_pass == f_pass:
                if len(u_pass)>=3:
                    user= User.objects.create_user(first_name=f_name,last_name=l_name,username=u_name, password= u_pass)
                    user.save()
                    return redirect('login_page')
                else:
                    messages.info(request,"Password less than 8 characters")
                    return render(request, 'register.html')
            else:
                messages.info(request,"Password doesn't match")
                return render(request, 'register.html')
        else:
            messages.info(request,"Please! fill all fields")
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(user_board)
        else:
            messages.info(request,"username/pasword didn't match")
            return render(request, 'log.html')
    else:
        return render(request, 'log.html')


def logout_view(request):
    logout(request)
    return redirect(index)


def index(request):
    return render(request, 'index.html')

def user_board(request):
    todos= Todo.objects.filter(user= request.user)
    # context={'product': product}
    return render(request, 'user_board.html',{'todos': todos})

def addTodos(request):
    if request.method== 'POST':
        user=User.objects.get(username=request.user)
        title= request.POST['title']
        body= request.POST['textarea']
        ex= Todo(title=title, body=body, user=user)
        ex.save()
        return render(request, 'user_board.html')
    else:  
        return render(request, 'addTodo.html')

def todoDetails(request, id):
    details= Todo.objects.filter(id=id)
    return render(request, 'todo_details.html', {'details': details})


def delete(request, id):
    dele= Todo.objects.get(id=id)
    dele.delete()
    todos= Todo.objects.filter(user= request.user)
    return render(request, 'user_board.html', {'todos': todos})


def edit(request, id):
    edit=Todo.objects.get(id=id)    
    if request.method== 'POST':
        e_title=request.POST.get('title') 
        e_body= request.POST.get('textarea') 
        edit.title= e_title
        edit.body=e_body
        edit.save()
        return render(request,'user_board.html')
    return render(request, 'edit.html', {'todos': edit})