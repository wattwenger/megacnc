# Generated by Django 4.2.10 on 2024-02-23 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megacellcnc', '0012_alter_printersettings_printerhost_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='printersettings',
            name='CustomField1',
            field=models.CharField(default='deepcyclepower.com', max_length=150),
        ),
    ]