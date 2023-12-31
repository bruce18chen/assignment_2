# Generated by Django 4.2.1 on 2023-06-11 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0011_topic_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, unique_for_date='published'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
