# Generated by Django 5.1.7 on 2025-05-15 01:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignaciones', '0001_initial'),
        ('programacion', '0002_remove_programacion_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='programacion',
            name='asignacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='programacion', to='asignaciones.asignacion'),
            preserve_default=False,
        ),
    ]
