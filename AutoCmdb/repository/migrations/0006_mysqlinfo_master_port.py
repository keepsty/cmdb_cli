# Generated by Django 2.2 on 2019-07-29 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0005_auto_20190729_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysqlinfo',
            name='master_port',
            field=models.IntegerField(default=3306),
            preserve_default=False,
        ),
    ]
