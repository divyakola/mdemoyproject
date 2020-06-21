from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.
class insert(View):
    def get(self,request):
        return render(request,'input.html')
class addition(View):
    def get(self,request):
        a=int(request.GET['fn'])
        b=int(request.GET['ln'])
        return HttpResponse("the sum is: "+str(a+b))
