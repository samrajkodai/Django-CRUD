# Generated by Django 4.0.5 on 2022-07-13 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_blog_delete_taskdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeID', models.IntegerField(default=0)),
                ('Name', models.CharField(default='SOME STRING', max_length=20)),
                ('Age', models.IntegerField()),
                ('Location', models.CharField(default='SOME STRING', max_length=20)),
                ('Designation', models.CharField(default='SOME STRING', max_length=20)),
                ('Salary', models.IntegerField(default=0)),
                ('PhoneNumber', models.IntegerField(default=0)),
                ('EmailID', models.CharField(default='SOME STRING', max_length=20)),
            ],
            options={
                'db_table': 'employee_details',
            },
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
