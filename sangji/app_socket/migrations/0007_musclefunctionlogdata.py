# Generated by Django 4.0.6 on 2022-10-27 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_socket', '0006_rename_rom_isokinetic_1rm_userinfomation_rom_isokinetic_1rm'),
    ]

    operations = [
        migrations.CreateModel(
            name='MuscleFunctionLogData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='사용자')),
                ('exercise_type', models.CharField(max_length=50, verbose_name='운동 종류')),
                ('log', models.TextField(verbose_name='측정기록')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='측정일시')),
            ],
        ),
    ]
