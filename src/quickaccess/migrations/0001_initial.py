# Generated by Django 5.0.1 on 2024-02-04 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MMDQuickFavorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccessKey', models.CharField(default='', max_length=100)),
                ('Username', models.CharField(default='', max_length=100)),
                ('Data', models.JSONField(default='{}')),
            ],
        ),
    ]
