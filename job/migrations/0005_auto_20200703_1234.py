# Generated by Django 3.0.3 on 2020-07-03 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20200703_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='published_at',
            field=models.DateTimeField(),
        ),
    ]
