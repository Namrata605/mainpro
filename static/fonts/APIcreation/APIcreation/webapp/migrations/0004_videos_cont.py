# Generated by Django 2.2 on 2020-03-30 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_videos_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='cont',
            field=models.ImageField(default=1, upload_to='pics'),
            preserve_default=False,
        ),
    ]
