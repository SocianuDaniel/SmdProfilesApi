# Generated by Django 5.1.2 on 2025-02-07 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_user_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.IntegerField(choices=[(0, 'SUPERUSER'), (1, 'OWNER'), (2, 'REGIONMANAGER'), (3, 'ZONEMANAGER'), (4, 'STOREMANAGER'), (5, 'ASSISTENTSTOREMANAGER'), (6, 'SHIFT'), (7, 'HOSTESS'), (8, 'CREW')], default=8),
        ),
    ]
