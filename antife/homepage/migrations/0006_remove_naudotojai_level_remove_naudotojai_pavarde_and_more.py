# Generated by Django 5.0.3 on 2024-03-15 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_alter_naudotojai_options_alter_naudotojai_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='naudotojai',
            name='level',
        ),
        migrations.RemoveField(
            model_name='naudotojai',
            name='pavarde',
        ),
        migrations.RemoveField(
            model_name='naudotojai',
            name='vardas',
        ),
    ]
