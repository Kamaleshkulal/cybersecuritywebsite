# Generated by Django 4.1.1 on 2022-09-12 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_alter_forms_branch_alter_forms_college'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forms',
            old_name='CGPA',
            new_name='cgpa',
        ),
    ]
