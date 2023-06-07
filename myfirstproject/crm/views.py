from django.shortcuts import render
from .models import Order
from django.shortcuts import render
# Create your views here.
def firstpage(request):
    object_list = Order.objects.all()
    return render(request, './index.html', { 'object_list': object_list })


def home(request):
    return render(request, 'home.html',{'hello': 'salam kirya' })

def hello(request):
    msg = request.GET['message']
    return render(request, 'anotherpage.html',{'message':msg})
def skam(request):
    return render(request, 'skam.html')

def response(request):
    name = request.POST['name']
    phone = request.POST ['phone']
    element = Order(order_name = name, order_phone = phone)
    element.save()
    return render(request, 'response.html', {'name': name,
                                             'phone': phone})