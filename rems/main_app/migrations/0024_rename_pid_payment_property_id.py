# Generated by Django 5.0.3 on 2024-05-11 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0023_alter_payment_client_nid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='pid',
            new_name='property_id',
        ),
    ]