# Generated by Django 2.0.3 on 2018-07-01 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180701_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainimg',
            name='mainImg',
            field=models.ImageField(upload_to='main'),
        ),
        migrations.AlterField(
            model_name='work',
            name='main_img',
            field=models.ImageField(upload_to='work'),
        ),
    ]
