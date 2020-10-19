# Generated by Django 3.0.3 on 2020-07-20 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
            ],
            options={
                'verbose_name': 'Info',
                'verbose_name_plural': 'Information',
            },
        ),
    ]