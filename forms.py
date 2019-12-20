from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(label='Your name:',max_length=100)
    regNo = forms.CharField(label='Registration Number:',max_length=100)
    classs = forms.CharField(label='Class:',max_length=100)


class TeacherForm(forms.Form):
    name = forms.CharField(label='Your name:',max_length=100)
    empId = forms.CharField(label='Employee Id:',max_length=100)
    sub = forms.CharField(label='Subject:',max_length=100)
