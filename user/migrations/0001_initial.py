# Generated by Django 3.1.5 on 2021-01-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=200, unique=True, verbose_name='username')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='name')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='is superuser')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]