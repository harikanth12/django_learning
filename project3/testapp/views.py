from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.http import HttpResponse,Http404
from testapp.models import employee
from testapp.forms import EmployeeForm
# Create your views here.
def index(request,id):
    print(id)
    return HttpResponse("You're looking at question %s" % id)

def details(request,question_id,id):
    return HttpResponse("Your are at question no. %s ,id : %s" % (question_id, id))

def data(request):
    msg = ""
    try:
        emp = employee.objects.get(id=1)
        msg = "data retrived"
    except employee.DoesNotExist:
        msg = "id doesnot exits"
    return HttpResponse (msg)

def data1(request):
    emp = get_object_or_404(employee,id=1) ## if object is there returns the data other wise raise Http 404 error
    return HttpResponse(emp.ename)

def data2(request):
    emp = get_list_or_404(employee,id=1,ename="Hari")  ## get_list is used for filter the data ..if the list is empty it raise the 404 error
    for i in emp:
        i.ename
    return HttpResponse(emp[0])

def home(request):
    context = {
        'msg':"Hello good morning"
    }
    return render(request,'base.html',context)

def newmanager(request):
    emp = employee.objects.get_emp_eno()
    print(emp)
    return HttpResponse("Success")

from testapp.forms import EmployeeForm
def newform(request):
    context = {'form':"HTML Form"}
    # form = forms.EmployeeForm
    if request.method == "POST":
        # data = request.POST['data']
        # marks = request.POST['marks']
        # data = request.POST.cleaned_data['data']
        # marks = request.POST.cleaned_data['marks']
        form = EmployeeForm(request.POST)
        if form.is_valid():
            return HttpResponse("Logged in")
    return render(request,'index.html',context)

