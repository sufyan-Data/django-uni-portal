from django.contrib import admin
from .models import Student, LoginUser

# Register your models here.
admin.site.register(Student)
admin.site.register(LoginUser)
# admin.site.register(UploadedFileData)