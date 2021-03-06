# Generated by Django 2.0.5 on 2018-05-19 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_id', models.IntegerField(unique=True)),
                ('name', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_id', models.IntegerField(unique=True)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('building', models.ForeignKey(db_column='building_s_id', on_delete=django.db.models.deletion.CASCADE, to='core.Building', to_field='s_id')),
            ],
        ),
    ]
