# Generated by Django 4.2.7 on 2023-11-11 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_content_post_content_rename_date_post_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumb',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]