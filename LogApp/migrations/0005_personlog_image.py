# Generated by Django 3.2.7 on 2021-09-08 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LogApp', '0004_alter_personlog_mask'),
    ]

    operations = [
        migrations.AddField(
            model_name='personlog',
            name='image',
            field=models.CharField(max_length=255, null=True),
        ),
    ]