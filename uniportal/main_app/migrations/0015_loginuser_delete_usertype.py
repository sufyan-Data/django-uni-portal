# Generated by Django 4.1.5 on 2023-02-06 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_alter_usertype_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('login_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=60)),
                ('email', models.CharField(default='', max_length=60)),
                ('password', models.CharField(default='', max_length=60)),
                ('user_type', models.CharField(choices=[('HOD', 'HOD'), ('Student', 'Student'), ('Teacher', 'Teacher')], default='', max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='UserType',
        ),
    ]
