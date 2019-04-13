# Generated by Django 2.1.3 on 2018-12-16 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20181210_0230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alcohol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('degree', models.IntegerField(default=0)),
                ('value', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
            ],
        ),
    ]