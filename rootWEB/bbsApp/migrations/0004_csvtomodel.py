# Generated by Django 3.2.5 on 2021-08-24 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbsApp', '0003_timeline'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsvToModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickName', models.CharField(max_length=50)),
                ('profileImg', models.CharField(max_length=50)),
                ('marriage', models.CharField(max_length=50)),
            ],
        ),
    ]