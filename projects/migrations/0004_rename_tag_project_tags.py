# Generated by Django 3.2.6 on 2022-01-16 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20220116_0102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tag',
            new_name='tags',
        ),
    ]
