# Generated by Django 2.2 on 2019-07-31 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0019_auto_20190731_0921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dbgranthistory',
            old_name='database_ip',
            new_name='db_ip',
        ),
        migrations.AlterUniqueTogether(
            name='dbgranthistory',
            unique_together={('db_ip', 'db_username', 'port', 'db_permission', 'host_ip')},
        ),
    ]
