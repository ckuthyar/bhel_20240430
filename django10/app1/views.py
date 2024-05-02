from django.shortcuts import render
def home(request):
    fact=1
    n=6
    for i in range(1,n+1,1):
        fact=fact*i
    print(fact)
    return render(request,'app1/index.html',{'param1':fact})