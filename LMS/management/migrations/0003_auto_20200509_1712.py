# Generated by Django 3.0.3 on 2020-05-09 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20200509_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowed',
            name='issuedate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
