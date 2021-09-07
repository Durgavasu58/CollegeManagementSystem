from django.urls import path
from . import views
from .views import * 

urlpatterns=[

    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('adminpage/',views.admin,name='adminpage'),
    path('lecturer/',views.lecturer,name='lecturer'), #getting individual lecturer data
    path('student/',views.student,name='student'), #getting individual student data
    path('staff/',views.StaffMain,name='staffmain'), #getting individual staff data
    path('dashboard/',views.dashboard,name='dashboard'),

    # ==========================Lecturer Views============================
    path('lectreg/',views.LecturerReg,name='lectreg'),
    path('Lectlist/',views.Lectlist.as_view(),name='lectlist'),
    path('letupdate/<int:pk>/',views.LectUpdate.as_view(),name='letupdate'),
    path('letdelete/<int:pk>/',views.LectDelete.as_view(),name='letdelete'),


    # ==========================Student Views============================
    path('studentreg/',views.Studentreg,name='studreg'),
    path('Studlist/',views.StudentList.as_view(),name='studlist'),
    path('Studupdate/<int:pk>/',views.StudentUpdate.as_view(),name='stdupdate'),
    path('Studdelete/<int:pk>/',views.StudentDelete.as_view(),name='stddelete'),

    # ==========================Staff Views============================
    path('staffreg/',views.Staffreg,name='staffreg'),
    path('details/',views.OtherDetails.as_view(),name='other_details'), #staff list
    path('otherupdate/<int:pk>/',views.StaffUpdate.as_view(),name='other_update'),
    path('otherdelete/<int:pk>/',views.StaffDelete.as_view(),name='other_delete'),
    
    # ==========================Department Views============================
    path('DepartReg/',views.DepartmentReg,name='departreg'),
    path('Departlist/',views.Departlist.as_view(),name='departlist'),

    # ==========================College Views============================
    path('ColReg/',views.CollegeReg,name='colreg'),
    path('Collist/',views.collegelist.as_view(),name='collist'),

    # ==========================Branch Views============================
    path('BranchReg/',views.BranchReg,name='Branchreg'),
    path('Branchlist/',views.Branchlist.as_view(),name='Branchlist'),

    # ==========================Subject Views============================
    path('SubjectReg/',views.SubjReg,name='Subjreg'),
    path('Subjectlist/',views.Subjlist.as_view(),name='Subjlist'),

    # ==========================Fee Views============================
    path('FeeReg/',views.FeeReg,name='feereg'),
    path('Feelist/',views.Feelist.as_view(),name='feelist'),

    # ==========================Salary Views============================
    path('SalaryReg/',views.SalaryReg,name='salaryreg'),
    path('Salarylist/',views.Salarylist.as_view(),name='salarylist'),

    # ==========================Result Views============================
    path('ResultReg/',views.ResultReg,name='resultreg'),
    path('Resultlist/',views.Resultlist.as_view(),name='resultlist'),

    # ==========================Time Table Views============================
    path('timetableReg/',views.TimetableReg,name='timetablereg'),
    path('timetablelist/',views.Timetablelist.as_view(),name='timetablelist'),

]