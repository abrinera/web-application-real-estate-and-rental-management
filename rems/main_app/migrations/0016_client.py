# Generated by Django 5.0.3 on 2024-05-08 15:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_remove_rental_img3_remove_rental_img4_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CLient',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.IntegerField()),
                ('age', models.IntegerField()),
                ('nid', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('gender', models.CharField(max_length=10)),
                ('job', models.CharField(max_length=50)),
                ('date_of_birth', models.CharField(max_length=50)),
                ('property_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.property')),
                ('username', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
