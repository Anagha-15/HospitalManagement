# Generated by Django 4.1.2 on 2022-10-17 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_rename_dep_description_department_dep_discription'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Department',
            new_name='Departments',
        ),
        migrations.RenameField(
            model_name='departments',
            old_name='dep_discription',
            new_name='dep_discriptions',
        ),
    ]
