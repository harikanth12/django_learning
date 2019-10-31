from django.shortcuts import render
from praticeapp import forms

# Create your views here.

def index(request):
    form = forms.StudentForm()
    if request.method == "POST":
        form = forms.StudentForm(request.POST)
        # if form.is_valid():
        #     print("Validations Success")
        #     print('Name',form.cleaned_data['name'])
        #     print('Marks',form.cleaned_data['marks'])
    return render(request,'reg.html',context={'form':form})

def feedback(request):
    form = forms.FeedbackForm()
    if request.method == "POST":
        form = forms.FeedbackForm(request.POST)
        # print(form)
        if form.is_valid():
            print("hello")
    return render(request,'reg12.html',{'form':form})

