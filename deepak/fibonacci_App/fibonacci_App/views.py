import timeit
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def logic(request):
    n = request.GET.get('text', 'default')
    print(n)
    value=n

    def Fibonacci(n):
        if n < 0:
            print("Incorrect input")
            # First Fibonacci number is 0
        elif n == 0:
            return 0
        # Second Fibonacci number is 1
        elif n == 1:
            return 1
        else:
            return Fibonacci(n - 1) + Fibonacci(n - 2)

            # Driver Program

  #  print(Fibonacci(9))
    params ={'value':Fibonacci(int(value))}
    return render(request,'logic.html',params)