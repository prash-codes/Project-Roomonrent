# Generated by Django 4.0.4 on 2022-05-27 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ror', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_image',
            field=models.ImageField(upload_to='room_images/'),
        ),
    ]