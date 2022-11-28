from tkinter.ttk import Style
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
from .models import Test, SumTwoIntegers
from .forms import UserForm

# no connnection to db
# def index(request):
#     if request.method == "POST":
#         value1 = request.POST.get("field1")
#         value2 = request.POST.get("field2")
#         # age = request.POST.get("age")     # получение значения поля age
#         return HttpResponse("<h2>Result: {0}</h2>".format(int(value1) + int(value2)))
        
#     else:
#         userform = UserForm()
#         return render(request, "index.html", {"form": userform})


#with connnection to db
def index(request):
        if request.method == 'POST':
            if request.POST.get('field1') and request.POST.get('field2'):
                post=SumTwoIntegers()
                post.field1= request.POST.get('field1')
                post.field2= request.POST.get('field2')
                post.result= request.POST.get('result')
                value1 = request.POST.get("field1")
                value2 = request.POST.get("field2")
                result = request.POST.get(int(value1) + int(value2))
                post.save()
                
                return HttpResponse("<h2>Result: {0}</h2>".format(result)) 
        
        else:
                return render(request,'index.html')

