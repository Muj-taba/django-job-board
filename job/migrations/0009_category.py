# Generated by Django 3.0.3 on 2020-07-03 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_auto_20200703_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]
