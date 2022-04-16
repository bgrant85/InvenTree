# Generated by Django 3.2.4 on 2021-09-25 16:08

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0041_alter_company_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplierpart',
            name='note',
            field=markdownx.models.MarkdownxField(blank=True, help_text='Part notes - supports Markdown formatting', null=True, verbose_name='Notes'),
        ),
    ]