# Generated by Django 5.0.3 on 2024-05-03 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_rename_img1_property_image1_alter_property_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='img2',
            new_name='image2',
        ),
        migrations.RemoveField(
            model_name='property',
            name='img3',
        ),
        migrations.RemoveField(
            model_name='property',
            name='img4',
        ),
        migrations.RemoveField(
            model_name='property',
            name='img5',
        ),
    ]