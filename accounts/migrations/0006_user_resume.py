# Generated by Django 2.1.7 on 2022-12-12 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20221212_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='resume',
            field=models.FileField(default='APPENDIX.pdf', upload_to='resumes'),
        ),
    ]
