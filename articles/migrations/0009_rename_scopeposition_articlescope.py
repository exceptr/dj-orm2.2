# Generated by Django 4.0.6 on 2022-07-15 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_rename_scope_scopeposition_tag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ScopePosition',
            new_name='ArticleScope',
        ),
    ]
