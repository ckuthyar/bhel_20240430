from django.shortcuts import render
def home(request):
    list1=[]
    for i in range(0,11,2):
        list1.append(i)
    return render(request,'app2/index.html',{'param1':list1})