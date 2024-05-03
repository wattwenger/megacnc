# Generated by Django 4.2.10 on 2024-05-03 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megacellcnc', '0018_batteries_cells_battery'),
    ]

    operations = [
        migrations.AddField(
            model_name='cells',
            name='bat_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cells',
            name='bat_position',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
