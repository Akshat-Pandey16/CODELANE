# Generated by Django 3.1.2 on 2020-11-28 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='link',
            field=models.URLField(),
        ),
    ]
