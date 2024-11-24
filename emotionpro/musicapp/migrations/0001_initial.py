# Generated by Django 5.1 on 2024-11-20 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('profilepic', models.FileField(blank=True, null=True, upload_to='profile/')),
            ],
        ),
    ]
