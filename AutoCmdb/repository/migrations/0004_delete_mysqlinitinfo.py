# Generated by Django 2.2 on 2019-07-25 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0003_remove_mysqlinitinfo_hostname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MysqlInitInfo',
        ),
    ]
