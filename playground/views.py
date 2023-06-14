from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request handler
def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    #return render(request, 'hello.html', {'name': 'Django'})
    #pull data from database
    #transform data
    #send email
    #return HttpResponse('Hello World!')
    x = calculate()
    return render(request, 'hello.html', {'name': 'Django'})
