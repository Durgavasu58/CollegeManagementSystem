from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Student,Lecturer,StaffMembers,Depart,College,Branch,Subject,Fee,Salary,Results,TimeTable
from django.db import transaction



class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class":"form-control"
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class":"form-control"
        })
    )

class SignupForm(UserCreationForm):
    username = forms.CharField(
        widget= forms.TextInput(attrs={
            "class":"form-control"
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class":"form-control"
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class":"form-control"
        })
    )
    email = forms.CharField(
        widget= forms.TextInput(attrs={
            "class":"form-control"
        })
    )

    class Meta:
        model = User
        fields = ('username','email','password1','password2','is_lecturer','is_student','is_staff')



class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = '__all__'
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class StaffForm(forms.ModelForm):
    class Meta:
        model = StaffMembers
        fields = '__all__'


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Depart
        fields = '__all__'        

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = '__all__'          

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'          


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'  

class FeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = '__all__'  
               

class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = '__all__'  

class ResultForm(forms.ModelForm):
    class Meta:
        model = Results
        fields = '__all__'  
               

class TimeTableForm(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = '__all__'         