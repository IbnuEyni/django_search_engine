# Generated by Django 5.1.1 on 2024-09-11 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file_type', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
    ]
