# Generated by Django 4.0.6 on 2022-07-15 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_remove_scope_articles_article_scopes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Scope',
            new_name='Tag',
        ),
    ]
