# Generated by Django 4.1.5 on 2023-02-07 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_loginuser_delete_usertype'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadedFileData',
        ),
        migrations.RenameField(
            model_name='loginuser',
            old_name='login_id',
            new_name='user_id',
        ),
        migrations.RemoveField(
            model_name='loginuser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='loginuser',
            name='password',
        ),
        migrations.RemoveField(
            model_name='loginuser',
            name='username',
        ),
        migrations.AddField(
            model_name='loginuser',
            name='user_email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='loginuser',
            name='user_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='loginuser',
            name='user_password',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='student_contact',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='student_email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='student_roll_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_batch',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_enrol_no',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
