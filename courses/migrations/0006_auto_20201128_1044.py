# Generated by Django 3.1.3 on 2020-11-28 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20201128_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='link',
            field=models.URLField(max_length=500),
        ),
    ]
