# Generated by Django 4.1.7 on 2023-02-19 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0006_alter_project_acquisition_date_alter_wtg_cod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='acquisition_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='wtg',
            name='COD',
            field=models.DateTimeField(),
        ),
    ]
