# Generated by Django 4.2.10 on 2024-05-03 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('megacellcnc', '0020_alter_cells_bat_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cells',
            name='bat_id',
        ),
    ]
