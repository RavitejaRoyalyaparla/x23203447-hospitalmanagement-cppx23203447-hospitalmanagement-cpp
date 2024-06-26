# Generated by Django 5.0.3 on 2024-04-07 06:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_bed'),
    ]

    operations = [
        migrations.CreateModel(
            name='BedAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bed')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.patient')),
            ],
        ),
    ]
