# Generated by Django 3.2.12 on 2023-06-27 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrapp', '0007_auto_20230627_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcodedata',
            name='admin_at',
            field=models.DateTimeField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='qrcodedata',
            name='receiver_at',
            field=models.DateTimeField(blank=True, default='', null=True),
        ),
    ]
