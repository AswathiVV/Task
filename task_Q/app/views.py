from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1(request):
    return HttpResponse("fun1")
def fun2(request):
    return HttpResponse("fun2")
def index_page(request):
    return render(request,'index.html')
def fun3(request,a,b):
    return HttpResponse(a)

def fun4(request,a,b,c):
    if a>b and a>c:
        return HttpResponse(a)
    elif b>a and b>c:
        return HttpResponse(a)
    else:
        return HttpResponse(c)
    
def bonus(request,a,b):    
    if b>=5 :
        bonus=0.05*a
        return HttpResponse(f"Net Bonus Amount:{bonus:.5}")
    else:
        return HttpResponse("You are not eligible for bonus")
def divisable(request,a) :
        if a%3==0:
            return HttpResponse("Divisible")
        else:
            return HttpResponse("Not Divisible")   
def bill(request,a):         
        if a<100:
            return HttpResponse("No Charge")
        elif a>100 and a<200:
            fee=5*(a-100)
            return HttpResponse(f"Fee:{fee}")   
        else:
            fee=((a-200)*10)+500
            return HttpResponse(f"Fee:{fee}") 
def city(request,a) :
        if a=="Delhi":
            return HttpResponse("Red Fort")
        elif a=="Agra":
            return HttpResponse("Taj Mahal")
        elif a=="Jaipur":
            return HttpResponse("Jal Mahal")   

def tax(request,a):
        if a>100000:
            Tax=a*.15
            return HttpResponse(f"Road Tax :{Tax}")
        elif a<=100000 and a>=50000:
            Tax=a*.10
            return HttpResponse(f"Road Tax :{Tax}")
        else:
            Tax=a*.05
            return HttpResponse(f"Road Tax :{Tax}") 
        
def day(request,a):
        if a==1:
            return HttpResponse("Sunday")
        elif a==2:
            return HttpResponse("Monday")
        elif a==3:
            return HttpResponse("Tuesday")        
        elif a==4:
            return HttpResponse("Wednessday")
        elif a==3:
            return HttpResponse("Thursday")   
        elif a==3:
            return HttpResponse("Friday")                  
        elif a==3:
            return HttpResponse("Saturday")       
        else:
            return HttpResponse("Invalid no.")                      