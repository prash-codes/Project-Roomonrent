# Generated by Django 4.0.4 on 2022-05-27 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ror', '0002_alter_room_room_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('massage', models.CharField(max_length=500)),
            ],
        ),
    ]
