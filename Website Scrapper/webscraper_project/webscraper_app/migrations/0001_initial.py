# Generated by Django 4.2.9 on 2024-01-17 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('string_name', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
