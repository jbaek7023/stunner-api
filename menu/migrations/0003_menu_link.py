# Generated by Django 2.0.3 on 2018-04-20 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20180420_0553'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
