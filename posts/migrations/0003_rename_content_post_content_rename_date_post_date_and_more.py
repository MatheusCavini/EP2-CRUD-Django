# Generated by Django 4.2.7 on 2023-11-11 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_content_post_content_rename_date_post_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Title',
            new_name='title',
        ),
    ]
