# Generated by Django 3.0.7 on 2020-06-29 11:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('login_date', models.DateField(default=django.utils.timezone.now)),
                ('request_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]