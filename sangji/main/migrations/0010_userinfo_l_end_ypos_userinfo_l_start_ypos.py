# Generated by Django 4.0.6 on 2022-10-13 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_isotonic_b_end_ypos_userinfo_b_end_ypos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='l_end_ypos',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='l_start_ypos',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
