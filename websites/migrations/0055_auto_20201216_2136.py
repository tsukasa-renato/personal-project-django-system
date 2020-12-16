# Generated by Django 3.0.8 on 2020-12-16 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0054_auto_20201215_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='discord',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='twitch',
        ),
        migrations.AddField(
            model_name='contacts',
            name='social_media_text',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='whatsapp_text',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
