# Generated by Django 5.1.1 on 2024-09-19 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_habilidades_alter_empleado_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='person.habilidades'),
        ),
    ]
