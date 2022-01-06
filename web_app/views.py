from django.shortcuts import render,HttpResponse,redirect
from . forms import my_first_form
from . models import form_models

# Create your views here.

def index(request):
    f = my_first_form()
    return render(request, 'index.html', {"f":f})


def save_data(request):
    fatch_data = my_first_form(request.POST)
    if fatch_data.is_valid():
        fatch_data.save()
    return redirect("index")

def updated_data(request):
    tabel_1_row_data = form_models.objects.get(id =2)   #id=2 ar row nea aslo

    fatch_data = my_first_form(request.POST, instance=tabel_1_row_data) # id=2 ar man update korlo with instance key word

    if fatch_data.is_valid():
        fatch_data.save()

    return redirect("index")


def delete_data(request):
    value_id = request.POST.get('id_value')

    d = form_models(id = value_id)
    d.delete()


    return redirect("index")
