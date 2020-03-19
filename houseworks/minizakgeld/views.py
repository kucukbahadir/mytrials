from django.shortcuts import render,redirect
from .models import Zakgeld
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
   return render(request,"index.html")


def minizakgeld_add (request):
    if request.method == "POST":
        person = request.POST['person']
        task = request.POST['task']
        amount = request.POST['amount']

        minizakgeld=Zakgeld(person=person, task=task, amount=amount)
        minizakgeld.save()

        return redirect('/')
    
    return render(request, "minizakgeld_add.html")



def minizakgeld_details (request):
    Zakgelds=Zakgeld.objects.all()
    
    context = {
        "Zakgelds": Zakgelds
    }
    return render(request,"minizakgeld_details.html", context)


def person_1 (request):
    
    return render(request, "person_1.html")