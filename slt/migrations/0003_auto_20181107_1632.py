# Generated by Django 2.0.7 on 2018-11-07 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slt', '0002_auto_20181107_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='body',
            field=models.TextField(),
        ),
    ]
