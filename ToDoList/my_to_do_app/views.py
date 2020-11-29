from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import*

def index(request):
	#return HttpResponse("my_to_do_app first padge")
        return render(request, 'my_to_do_app/index.html')

def createTodo(request):
        user_input_str = request.POST['todoContent']
        
        # DB에 저장
        new_todo = Todo(content = user_input_str)
        new_todo.save()

        return HttpResponse("create ToDo !! =>" + user_input_str )
