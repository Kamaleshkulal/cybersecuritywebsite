# Generated by Django 4.1.1 on 2022-09-12 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_alter_forms_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forms',
            name='Branch',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='forms',
            name='College',
            field=models.CharField(max_length=50),
        ),
    ]
