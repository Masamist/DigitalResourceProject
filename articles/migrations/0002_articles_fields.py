# Generated by Django 4.1.3 on 2022-11-20 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='fields',
            field=models.JSONField(null=True),
        ),
    ]