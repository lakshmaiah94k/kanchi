from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_code = models.CharField(max_length=15)

    def __str__(self):
        return self.department_name


class Staff(models.Model):
    staff_name = models.CharField(max_length=100)
    staff_email = models.EmailField()
    staff_father_name = models.CharField(max_length=100)
    staff_mother_name = models.CharField(max_length=100)
    staff_profile_photo = models.ImageField(upload_to='images/')
    staff_mobile = models.CharField(max_length=100)
    department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.staff_name


class StudentApp(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    ssc_memo = models.ImageField(upload_to='images/')
    inter_memo = models.ImageField(upload_to='images/')
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.Student_name


class StudentReg(models.Model):
    student_apps = models.OneToOneField(StudentApp, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    student_father_name = models.CharField(max_length=100)
    student_mother_name = models.CharField(max_length=100)
    student_mobile = models.CharField(max_length=100)
    student_profile_photo = models.ImageField(upload_to='images/')
    department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name
