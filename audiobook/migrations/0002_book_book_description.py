# Generated by Django 5.0 on 2023-12-21 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audiobook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_description',
            field=models.TextField(default='empty'),
            preserve_default=False,
        ),
    ]
