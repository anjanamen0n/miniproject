# Generated by Django 4.2.3 on 2023-07-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectorapp', '0003_rename_courses_course_course_rename_tasks_task_task_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='course',
            new_name='Course',
        ),
        migrations.RemoveField(
            model_name='content',
            name='d_user',
        ),
        migrations.RemoveField(
            model_name='course',
            name='d_user',
        ),
        migrations.RemoveField(
            model_name='day',
            name='d_user',
        ),
        migrations.RemoveField(
            model_name='task',
            name='d_user',
        ),
        migrations.AlterField(
            model_name='task',
            name='Task',
            field=models.CharField(max_length=250),
        ),
    ]
