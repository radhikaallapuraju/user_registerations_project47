# Generated by Django 4.1.7 on 2023-05-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_webpage_access_records'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]