# Generated by Django 3.0.8 on 2020-07-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('day', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
            ],
        ),
    ]
