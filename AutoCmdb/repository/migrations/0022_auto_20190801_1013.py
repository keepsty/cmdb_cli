# Generated by Django 2.2 on 2019-08-01 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0021_auto_20190801_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbgranthistory',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='dbgranthistory',
            name='judge_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]