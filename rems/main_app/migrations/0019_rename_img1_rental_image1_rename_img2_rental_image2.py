# Generated by Django 5.0.3 on 2024-05-08 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_rename_client_info_client'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rental',
            old_name='img1',
            new_name='image1',
        ),
        migrations.RenameField(
            model_name='rental',
            old_name='img2',
            new_name='image2',
        ),
    ]