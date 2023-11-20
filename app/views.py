from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':12,'b':448,'c':77}
    return render(request,'condition.html',d)
