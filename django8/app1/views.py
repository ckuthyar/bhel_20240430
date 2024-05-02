from django.shortcuts import render
def home(request):
    n=6
    fact=1
    for i in range (1,n+1,1):
        fact=fact*i
    return render(request,'app1/index.html',{'param1':fact})