# Generated by Django 5.1 on 2024-08-10 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(help_text='شماره موبایل', max_length=11, unique=True)),
                ('password', models.CharField(help_text='رمز عبور', max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'همکاران ',
                'verbose_name_plural': 'همکاران',
            },
        ),
        migrations.AlterModelOptions(
            name='peoplemodel',
            options={'verbose_name': 'کاربران ', 'verbose_name_plural': 'کاربران'},
        ),
    ]
