# Generated by Django 4.1.5 on 2023-02-06 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_usertype_delete_loginuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertype',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]