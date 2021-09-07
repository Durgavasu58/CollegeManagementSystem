from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin=models.BooleanField('Register as admin',default=False)
    is_lecturer=models.BooleanField('Register as Lecturer',default=False)
    is_student=models.BooleanField('Register as Student',default=False)
    is_staff=models.BooleanField('Register as Staff',default=False)
class College(models.Model):
    clg_name = models.CharField(max_length=20, primary_key=True,blank=True)

    def __str__(self):
        return self.clg_name

class Depart(models.Model):
    id = models.IntegerField(primary_key=True)
    clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
    dep_name = models.CharField(max_length=20)

    def __str__(self):
        return self.dep_name

class Branch(models.Model):
    id = models.IntegerField(primary_key=True)
    clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
    dep_name = models.ForeignKey(Depart, on_delete=models.CASCADE)
    bran_name = models.CharField(max_length=20)

    def __str__(self):
        return self.bran_name

class TimeTable(models.Model):
    # id = models.IntegerField(primary_key=True)
    clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
    dep_name = models.ForeignKey(Depart, on_delete=models.CASCADE)
    bran_name = models.ForeignKey(Branch, on_delete=models.CASCADE)
    # subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()

    def __str__(self)->str:
        return f'{self.time_start},{self.time_end}'

class Salary(models.Model):
    salary = models.FloatField(max_length=30)

    def __str__(self):
        return str(self.salary)


class Fee(models.Model):
    coll_fee=models.IntegerField()
    exam_fee=models.IntegerField()

    def __str__(self)->str:
        return f'{self.coll_fee},{self.exam_fee}'
    


class Subject(models.Model):
    #clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
    #dep_name = models.ForeignKey(Depart, on_delete=models.CASCADE)
    #stu_name = models.OneToOneField(Student, on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=20)
    #time_table = models.ForeignKey(TimeTable, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_name



results_choices = (
    ('1st class','Grade A'),
    ('2nd class','Grade B2'),
    ('3rd class','Grade C1'),
    ( '4th class','Grade C2'),
    ( 'Destinction','Grade D'),
    )


class Results(models.Model):
    #clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
    #dep_name = models.ForeignKey(Depart, on_delete=models.CASCADE)
    #stu_name = models.OneToOneField(Student, on_delete=models.CASCADE)
    #subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    result = models.CharField(max_length=100,choices=results_choices)

    def __str__(self):
        return self.result


class Student(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
	dep_name = models.ForeignKey(Depart, on_delete=models.CASCADE)
	subj_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
	stu_name = models.CharField(max_length=20)
	bran_name = models.ForeignKey(Branch, on_delete=models.CASCADE)
	table_name=models.ForeignKey(TimeTable,on_delete=models.CASCADE)
	result_name=models.ForeignKey(Results,on_delete=models.CASCADE)
	stu_fee=models.ForeignKey(Fee, on_delete=models.CASCADE)

	def __str__(self):
		return self.stu_name


job_choices = (
    ('CLERK','CLERK'),
    ('SWEEPER','SWEEPER'),
    ('WATCHMAN','WATCHMAN'),
    ('ACCOUNTANT','ACCOUNTANT')
    )

class StaffMembers(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=100,choices=job_choices)
    staff_salary = models.OneToOneField(Salary, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Lecturer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    clg_name = models.ForeignKey(College, on_delete=models.CASCADE,blank=True)
    dep_name = models.ForeignKey(Depart, on_delete=models.CASCADE)
    lect_name = models.CharField(max_length=20)
    lect_subj=models.ForeignKey(Subject,on_delete=models.CASCADE)	
    time_table = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    lect_sal=models.ForeignKey(Salary,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.lect_name




