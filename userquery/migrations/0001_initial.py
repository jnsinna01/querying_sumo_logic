# Generated by Django 3.1.2 on 2020-10-27 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SumoLogic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Query', models.CharField(max_length=200)),
                ('From_Date_Time', models.TextField()),
                ('To_Date_Time', models.TextField()),
            ],
        ),
    ]
