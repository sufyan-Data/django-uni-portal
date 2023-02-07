from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100, default="")
    student_email = models.CharField(max_length=100, default="")
    student_enrol_no = models.CharField(max_length=100, default=0)
    student_roll_no = models.IntegerField(default=0)
    student_batch = models.IntegerField(default=0)
    student_depart = models.CharField(max_length=100, default=0)
    student_contact = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media/studens/', default="")
    # pub_date = models.DateField()
   

    def __str__(self):
        return self.student_name

class LoginUser(models.Model):
    HeadofDepart = 'HOD'
    Student = 'Student'
    Teacher = 'Teacher'
    
    YEAR_IN_SCHOOL_CHOICES = [
        (HeadofDepart, 'HOD'),
        (Student, 'Student'),
        (Teacher, 'Teacher'),
    ]
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100, default="")
    user_email = models.CharField(max_length=100, default="")
    user_password = models.CharField(max_length=100, default="")
    user_type = models.CharField(max_length=10, choices=YEAR_IN_SCHOOL_CHOICES, default="")
    # user_type = models.IntegerField(default="")
    def __str__(self):
        return self.user_email

# class UploadedFileData(models.Model):
#     student_id = models.AutoField(primary_key=True)
#     student_name = models.CharField(max_length=100, default="")
#     student_email = models.CharField(max_length=100, default="")
#     student_enrol_no = models.CharField(default=0)
#     student_roll_no = models.IntegerField(default=0)
#     student_batch = models.IntegerField(default=0)
#     student_contact = models.IntegerField(default=0)

#     def __str__(self):
#         return self.student_name
