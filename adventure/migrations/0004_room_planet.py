# Generated by Django 3.0.3 on 2020-03-04 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0003_room_tile_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='planet',
            field=models.CharField(default='DEFAULT PLANET', max_length=32),
        ),
    ]