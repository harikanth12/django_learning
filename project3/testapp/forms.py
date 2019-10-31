from django import forms
from django.http import HttpResponse
class EmployeeForm(forms.Form):
    data = forms.CharField()
    marks = forms.IntegerField()


    def clean(self):
        cleaneddata = self.cleaned_data
        # print(cleaneddata.get('data'))
        if cleaneddata.get('data') != "Sunny":
            return HttpResponse("No data is available")
      
        



