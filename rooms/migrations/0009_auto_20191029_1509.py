# Generated by Django 2.2.5 on 2019-10-29 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0008_auto_20190925_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='guests',
            field=models.IntegerField(help_text='How many people will be staying?'),
        ),
    ]
