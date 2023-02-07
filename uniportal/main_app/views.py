import csv
from io import TextIOWrapper
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UploadFileForm
from .models import Student
import matplotlib.pyplot as plt
import io
import os
import base64
import pandas as pd
import seaborn as sns
from .models import LoginUser
from django.contrib.auth.decorators import login_required


# Create your views here.


def user_login(request):
    if request.method == 'POST':
        # Retrieve the email and password from the form
        email = request.POST['email']
        password = request.POST['password']

        # Attempt to authenticate the user by filtering the LoginUser model by email and password
        user = LoginUser.objects.filter(
            user_email=email, user_password=password).first()

        # If a user was found, proceed to render the appropriate dashboard
        if user is not None:
            request.session['user_id'] = user.user_id
            if user.user_type == 'Student':
                # Render the student dashboard and set the URL to 'stu_dashboard'
                return redirect('stu_dashboard')
            elif user.user_type == 'HOD':
                # Render the HOD dashboard and set the URL to 'hod_dashboard'
                return redirect('hod_dashboard')
            elif user.user_type == 'Teacher':
                # Render the teacher dashboard and set the URL to 'tea_dashboard'
                return redirect('tea_dashboard')
        # If no user was found, return an error message on the login page
        else:
            error_message = 'Invalid login credentials'
            return render(request, 'login.html', {'error_message': error_message})
    # If the request method is not POST, check if the user is already authenticated
    else:
        # Check if the user id is stored in the session
        if 'user_id' in request.session:
            # If the user id is stored in the session, retrieve the user information from the LoginUser model
            user = LoginUser.objects.filter(
                user_id=request.session['user_id']).first()
            # If the user was found, render the appropriate dashboard
            if user is not None:
                if user.user_type == 'Student':
                    # Set the URL to 'stu_dashboard'
                    return redirect('stu_dashboard')
                elif user.user_type == 'HOD':
                    # Set the URL to 'hod_dashboard'
                    return redirect('hod_dashboard')
                elif user.user_type == 'Teacher':
                    # Set the URL to 'tea_dashboard'
                    return redirect('tea_dashboard')
            else:
                return render(request, 'login.html')
        else:
            # If the user id is not stored in the session, render the login page
            return render(request, 'login.html')

    return render(request, 'login.html')


def user_logout(request):
    # Remove the user id from the session
    if 'user_id' in request.session:
        del request.session['user_id']
    # Redirect the user to the login page
    return redirect('/login')


def stu_dashboard_view(request):
    # Check if the user is logged in
    if 'user_id' not in request.session:
        return redirect('/login')
    # Code for rendering the student dashboard
    return render(request, 'stu_dashboard.html')


def hod_dashboard_view(request):
    # Check if the user is logged in
    if 'user_id' not in request.session:
        return redirect('/login')
    # Code for rendering the HOD dashboard
    return render(request, 'hod_dashboard.html')


def tea_dashboard_view(request):
    # Check if the user is logged in
    if 'user_id' not in request.session:
        return redirect('/login')
    # Code for rendering the teacher dashboard
    return render(request, 'tea_dashboard.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = TextIOWrapper(request.FILES['file'].file, encoding='utf-8')
            reader = csv.reader(file)
            header = next(reader)  # skip the first row with header
            try:
                for row in reader:
                    # validate the data in each row
                    if not row[0]:  # for example, validate column 1
                        raise ValueError("Column 1 is required")
                    # Check if the data already exists in the database
                    instance, created = Student.objects.update_or_create(
                        student_enrol_no=row[0], defaults={'student_name':row[1], 'student_email': row[2], 'student_roll_no': row[3], 'student_depart':row[4], 'student_batch':row[5], 'student_contact':row[6]})
                messages.success(request, 'File uploaded successfully.')
                return redirect('success_url')
            except Exception as e:
                messages.error(
                    request, 'An error occurred while processing the file: {}'.format(e))
    else:
        form = UploadFileForm()
    return render(request, 'uploadFiles.html', {'form': form})


def plot_view(request):
    ## ----- PLOT 1 ----- ##

    # # Retrieve data from database
    # data = UploadedFileData.objects.all().values()
    # # Plot data using Matplotlib
    # fig, ax = plt.subplots()
    # x_values = [d['student_enrol_no'] for d in data]
    # y_values = [d['student_name'] for d in data]
    # ax.bar(x_values, y_values)
    # ax.set_xlabel('X values')
    # ax.set_ylabel('Y values')
    # # Convert plot to image
    # buffer = io.BytesIO()
    # plt.savefig(buffer, format='png')
    # buffer.seek(0)
    # image_png = buffer.getvalue()
    # graphic = base64.b64encode(image_png)
    # graphic = graphic.decode('utf-8')
    # # Pass image data to template
    # context = {
    # 'graphic': graphic,
    # }
    # return render(request, 'plot.html', context)

    ## ----- PLOT 2 ----- ##

    # # Retrieve data from database
    # data = UploadedFileData.objects.all().values()
    # # Plot data using Matplotlib
    # fig, ax = plt.subplots(figsize=(8, 5))
    # y_values = [d['student_id'] for d in data]
    # x_values = range(len(y_values))
    # ax.bar(x_values, y_values)
    # ax.set_xlabel('Student Enrolment No')
    # ax.set_ylabel('Student ID')
    # ax.set_xticks(x_values)
    # ax.set_xticklabels([d['student_enrol_no'] for d in data])
    # plt.xticks(rotation=45, fontsize=6)
    # plt.yticks(fontsize=10)
    # # Convert plot to image
    # buffer = io.BytesIO()
    # plt.savefig(buffer, format='png')
    # buffer.seek(0)
    # image_png = buffer.getvalue()
    # graphic = base64.b64encode(image_png)
    # graphic = graphic.decode('utf-8')
    # # Pass image data to template
    # context = {
    # 'graphic': graphic,
    # }
    # return render(request, 'plot.html', context)

    ## ----- PLOT 3 ----- ##

    # Query the data from the database
    students = Student.objects.all()
    student_data = {
        'student_name': [student.student_name for student in students],
        'student_email': [student.student_email for student in students],
        'student_enrol_no': [student.student_enrol_no for student in students],
        'student_roll_no': [student.student_roll_no for student in students],
        'student_depart': [student.student_depart for student in students],
        'student_batch': [student.student_batch for student in students],
        'student_contact': [student.student_contact for student in students],
    }
    df = pd.DataFrame(student_data)

    # Use Seaborn to visualize the data
    plt1 = plt.figure(figsize=(5, 5))
    sns.countplot(x='student_depart', data=df)

    plt2 = plt.figure(figsize=(5, 5))
    sns.countplot(x='student_batch', data=df)

    # Save the plot to an image file
    plot_path = os.path.join('media/plot1.png')
    plt1.savefig(plot_path)

    plot_path2 = os.path.join('media/plot2.png')
    plt2.savefig(plot_path2)

    return render(request, 'plot.html')
