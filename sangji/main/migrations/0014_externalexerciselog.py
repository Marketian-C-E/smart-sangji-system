# Generated by Django 2.2.9 on 2023-09-13 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalExerciseLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30, verbose_name='사용자')),
                ('datetime', models.DateTimeField()),
                ('repetition', models.IntegerField()),
            ],
        ),
    ]
