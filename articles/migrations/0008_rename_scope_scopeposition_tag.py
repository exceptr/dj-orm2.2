# Generated by Django 4.0.6 on 2022-07-15 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_rename_scope_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scopeposition',
            old_name='scope',
            new_name='tag',
        ),
    ]