# Generated by Django 3.0 on 2020-12-05 16:53

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('blog', '0003_auto_20201205_0351'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
