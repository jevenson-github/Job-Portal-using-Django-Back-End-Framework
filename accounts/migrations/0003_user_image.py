# Generated by Django 2.1.7 on 2022-12-12 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190326_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='company-1.png', upload_to='img'),
        ),
    ]