# Generated by Django 5.0.4 on 2024-08-01 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('occupation', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('user_no', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]
