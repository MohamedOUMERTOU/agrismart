# Generated by Django 5.1.2 on 2024-11-02 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crops', '0002_crop_description_alter_crop_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image_url', models.URLField(blank=True, null=True)),
                ('video_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
