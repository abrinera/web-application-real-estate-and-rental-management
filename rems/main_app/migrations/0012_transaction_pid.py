# Generated by Django 5.0.3 on 2024-05-03 19:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_remove_transaction_property_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='pid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main_app.property'),
        ),
    ]
