# Generated by Django 5.1 on 2024-08-16 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_usermodel_alter_peoplemodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peoplemodel',
            name='count',
            field=models.CharField(help_text='تعداد', max_length=10),
        ),
    ]
