# Generated by Django 3.2.4 on 2021-06-27 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='fff', upload_to='pics'),
            preserve_default=False,
        ),
    ]
