# Generated by Django 3.0 on 2020-12-05 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='texto',
        ),
    ]
