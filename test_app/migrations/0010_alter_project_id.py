# Generated by Django 4.1.7 on 2023-02-19 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0009_alter_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.IntegerField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
