# Generated by Django 4.0.6 on 2022-07-14 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_scope_alter_article_options_scopeposition_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематики статьи'},
        ),
        migrations.AlterModelOptions(
            name='scopeposition',
            options={'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематики статьи'},
        ),
    ]