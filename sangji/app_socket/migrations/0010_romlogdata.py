# Generated by Django 2.2.9 on 2023-07-05 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_socket', '0009_alter_musclefunctionlogdata_extra'),
    ]

    operations = [
        migrations.CreateModel(
            name='ROMLogData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='사용자')),
                ('data', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]