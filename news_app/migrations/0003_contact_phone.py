# Generated by Django 5.0.2 on 2024-02-08 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_contact_alter_category_options_alter_news_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Phone'),
        ),
    ]
