# Generated by Django 5.0.1 on 2024-02-04 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickaccess', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mmdquickfavorites',
            name='Data',
            field=models.JSONField(default=dict),
        ),
    ]
