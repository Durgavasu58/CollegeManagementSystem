from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import  SignupForm,LoginForm
from django.contrib.auth import authenticate, login as Allogin,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.urls import reverse
from django.contrib import messages
from .models import *
from django.views.generic import CreateView
from .forms import LecturerForm,StudentForm,StaffForm,DepartmentForm,CollegeForm,BranchForm,SubjectForm,SalaryForm,ResultForm,TimeTableForm
from django.views.generic import ListView,CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    return render(request,'index.html')
 

def signout(request):
    logout(request)
    return redirect ('index')




def register(request):
    msg = None
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg  = 'user details invalid'
    else:
        form = SignupForm()
    return render(request,'register.html',{'form':form,'msg':msg})



def login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None and user.is_admin:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                Allogin(request,user)
                return redirect('adminpage')
            elif user is not None and user.is_lecturer:
                Allogin(request,user)
                return redirect('lecturer')
            elif user is not None and user.is_student:
                Allogin(request,user)
                return redirect('student')
            elif user is not None and user.is_staff:
                Allogin(request,user)
                return redirect('staffmain') 
            else:
                msg = 'Invalid Credentials'
    else:
        msg = 'error validating form'
    return render(request,'login.html',{'form':form,'msg':msg})    

def logout(request):
    return HttpResponseRedirect(reverse('login'))

def admin(request):
    return render(request,'admin/home.html')

def lecturer(request):
    lect = Lecturer.objects.get(user_id=request.user.id)
    context = {'lect':lect}
    return render(request,'lecturer/lecturer.html',context)

def student(request):
    student = Student.objects.get(user_id=request.user.id)
    context = {'student':student}
    return render(request,'student/student.html',context)

def StaffMain(request):
    staffdata = StaffMembers.objects.get(user_id=request.user.id)
    print(staffdata)
    context = {'staffdata':staffdata}
    return render(request,'staff/Staff.html',context)

def dashboard(request):
    return render(request,'dashboard.html')
# =========================  Department Views    =====================================================    
def DepartmentReg(request):
    context = {}
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('departlist')
    else:
        form = DepartmentForm()
    context['form']=form
    return render(request,'department/departmentreg.html',context)

class Departlist(ListView):
    model = Depart
    context_object_name='departlist'
    template_name = 'department/departlist.html'

# =========================  College Views    =====================================================    

def CollegeReg(request):
    context = {}
    form = BranchForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        form = BranchForm()
    context['form']=form
    return render(request,'college/collegereg.html',context)

class collegelist(ListView):
    model = College
    context_object_name='collist'
    template_name = 'college/collegelist.html'

# =========================  Branch Views    =====================================================    

def BranchReg(request):
    context = {}
    form = BranchForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Branchlist')
    else:
        form = BranchForm()
    context['form']=form
    return render(request,'branch/branchreg.html',context)


class Branchlist(ListView):
    model = Branch
    context_object_name='branchlist'
    template_name = 'branch/branchlist.html'


# =========================  Subject Views    =====================================================    

def SubjReg(request):
    context = {}
    form = SubjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Branchlist')
    else:
        form = SubjectForm()
    context['form']=form
    return render(request,'subject/subjectreg.html',context)


class Subjlist(ListView):
    model = Subject
    context_object_name='subjlist'
    template_name = 'subject/subjectlist.html'


# =========================  Fee Views    =====================================================    

def FeeReg(request):
    context = {}
    form = FeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Branchlist')
    else:
        form = FeeForm()
    context['form']=form
    return render(request,'Fee/feereg.html',context)


class Feelist(ListView):
    model = Fee
    context_object_name='feelist'
    template_name = 'Fee/feelist.html'

    # =========================  Salary Views    =====================================================    

def SalaryReg(request):
    context = {}
    form = SalaryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('salarylist')
    else:
        form = SalaryForm()
    context['form']=form
    return render(request,'Salary/salaryreg.html',context)

class Salarylist(ListView):
    model = Salary
    context_object_name='sallist'
    template_name = 'Salary/salarylist.html'

# =========================  Result Views    =====================================================    

def ResultReg(request):
    context = {}
    form = ResultForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('resultlist')
    else:
        form = ResultForm()
    context['form']=form
    return render(request,'Result/resultreg.html',context)

class Resultlist(ListView):
    model = Results
    context_object_name='resultlist'
    template_name = 'Result/resultlist.html'

    # =========================  TimeTable Views    =====================================================    

def TimetableReg(request):
    context = {}
    form = TimeTableForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('timetablelist')
    else:
        form = TimeTableForm()
    context['form']=form
    return render(request,'TimeTable/Timetablereg.html',context)

class Timetablelist(ListView):
    model = TimeTable
    context_object_name='tablelist'
    template_name = 'TimeTable/Timetablelist.html'


# =========================  Lecturer Views    =====================================================
def LecturerReg(request):
    context = {}
    form = LecturerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lectlist')
    else:
        form = LecturerForm()
    context['form']=form
    return render(request,'lecturer/lectreg.html',context)

class Lectlist(ListView):
    model = Lecturer
    context_object_name='lectlist'
    template_name = 'lecturer/lectlist.html'

class LectUpdate(UpdateView):
    model = Lecturer
    fields = '__all__'
    template_name = 'lecturer/lectupdate.html'
    success_url= reverse_lazy('lectlist')

class LectDelete(DeleteView):
    model = Lecturer
    template_name = 'lecturer/lectdelete.html'
    success_url = reverse_lazy('lectlist')

# =========================  Lecturer Views    =====================================================
def Studentreg(request):
    context = {}
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('studlist')
    else:
        form = StudentForm()
    context['form']=form
    return render(request,'student/studtreg.html',context)


class StudentList(ListView):
    model = Student
    context_object_name='stdlist'
    template_name = 'student/studentlist.html'

class StudentUpdate(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'student/studentupdate.html'
    success_url= reverse_lazy('studlist')

class StudentDelete(DeleteView):
    model = Student
    template_name = 'student/studentdelete.html'
    success_url = reverse_lazy('studlist')

# =========================  Staff Views    =====================================================    
def Staffreg(request):
    context = {}
    form = StaffForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('other_details')
    else:
        form = StaffForm()
    context['form']=form
    return render(request,'staff/staffreg.html',context)

class OtherDetails(ListView):
    model = StaffMembers
    context_object_name='stf_list'
    template_name = 'staff/stafflist.html'

class StaffUpdate(UpdateView):
    model = StaffMembers
    fields = '__all__'
    template_name = 'staff/staffupdate.html'
    success_url= reverse_lazy('other_details')

class StaffDelete(DeleteView):
    model = StaffMembers
    template_name = 'staff/staffdelete.html'
    success_url = reverse_lazy('other_details')