# Generated by Django 4.0.3 on 2022-03-11 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_rename_articles_articletag_article_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='article_tags',
            new_name='article',
        ),
    ]