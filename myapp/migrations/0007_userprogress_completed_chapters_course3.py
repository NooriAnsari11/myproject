# Generated by Django 4.2.3 on 2023-08-01 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_userprogress_completed_chapters_course2'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprogress',
            name='completed_chapters_course3',
            field=models.IntegerField(default=0),
        ),
    ]