# Generated by Django 5.0.3 on 2024-04-03 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grades',
            name='Value',
            field=models.IntegerField(default=0, verbose_name=0),
            preserve_default=False,
        ),
    ]
