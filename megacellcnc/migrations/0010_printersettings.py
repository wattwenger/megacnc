# Generated by Django 4.2.10 on 2024-02-22 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megacellcnc', '0009_celltestdata_charging_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrinterSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PrinterName', models.CharField(max_length=150)),
                ('PrinterHost', models.CharField(max_length=150)),
                ('IsDualLabel', models.IntegerField()),
                ('LabelWidth', models.FloatField()),
                ('LabelHeight', models.FloatField()),
                ('LabelRotation', models.IntegerField()),
            ],
        ),
    ]