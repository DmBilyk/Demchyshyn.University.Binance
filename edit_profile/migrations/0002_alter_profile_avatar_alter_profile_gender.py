# Generated by Django 4.2.11 on 2024-04-21 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edit_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/avatars/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'BTC'), (2, 'ETH')], null=True),
        ),
    ]