# Generated by Django 4.1.7 on 2023-04-01 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('phno', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=13)),
            ],
        ),
    ]