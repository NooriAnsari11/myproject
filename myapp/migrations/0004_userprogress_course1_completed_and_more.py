# Generated by Django 4.2.3 on 2023-07-24 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprogress',
            name='course1_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='course2_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='course3_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='course4_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='course5_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='course6_completed',
            field=models.BooleanField(default=False),
        ),
    ]