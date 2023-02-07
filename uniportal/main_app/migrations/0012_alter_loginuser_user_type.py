# Generated by Django 4.1.5 on 2023-02-05 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_rename_user_loginuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='user_type',
            field=models.CharField(choices=[('HOD', 'HOD'), ('Student', 'Student'), ('Teacher', 'Teacher')], default='', max_length=10),
        ),
    ]
