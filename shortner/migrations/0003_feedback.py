# Generated by Django 4.2.13 on 2024-05-25 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0002_alter_urldb_short_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('feedback', models.CharField(max_length=2000)),
            ],
        ),
    ]
