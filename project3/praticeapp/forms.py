from django import forms

class StudentForm(forms.Form):
    name = forms.CharField()
    marks = forms.IntegerField()

    def clean_name(self):
        print("bhbhjbhb")
        inputname = self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError("Minimum length of the name should be 4")
        return inputname
    
    def clean_marks(self):
        inputmarks = self.cleaned_data['marks']
        if inputmarks <500:
            raise forms.ValidationError("Minimum marks should be 500")
        return inputmarks

class FeedbackForm(forms.Form):
    uname = forms.CharField()
    remarks = forms.CharField()


    def clean_uname(self):
        inputname = self.cleaned_data['uname']
        if len(inputname)<4:
            raise forms.ValidationError("Minimum length of the name should be 4")
        return inputname 