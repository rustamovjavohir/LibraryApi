# Generated by Django 3.2.7 on 2021-10-03 03:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name=datetime.datetime(2021, 10, 3, 8, 18, 47, 75747))),
                ('created_by', models.IntegerField(default=-1)),
                ('is_deleted', models.IntegerField(default=0)),
                ('deleted_by', models.IntegerField(default=-1)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('page_count', models.IntegerField()),
                ('year', models.DateTimeField(default=datetime.datetime(2021, 10, 3, 8, 18, 47, 75747))),
                ('category', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name=datetime.datetime(2021, 10, 3, 8, 18, 47, 75747))),
                ('created_by', models.IntegerField(default=-1)),
                ('is_deleted', models.IntegerField(default=0)),
                ('deleted_by', models.IntegerField(default=-1)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('Role', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name=datetime.datetime(2021, 10, 3, 8, 18, 47, 75747))),
                ('created_by', models.IntegerField(default=-1)),
                ('is_deleted', models.IntegerField(default=0)),
                ('deleted_by', models.IntegerField(default=-1)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('profession', models.CharField(max_length=200)),
                ('is_active', models.IntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Kartoteka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name=datetime.datetime(2021, 10, 3, 8, 18, 47, 75747))),
                ('created_by', models.IntegerField(default=-1)),
                ('is_deleted', models.IntegerField(default=0)),
                ('deleted_by', models.IntegerField(default=-1)),
                ('get_time', models.DateTimeField(default=datetime.datetime(2021, 10, 3, 8, 18, 47, 77747))),
                ('return_time', models.DateTimeField(default=datetime.datetime(2021, 10, 18, 8, 18, 47, 77747))),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='books.book')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='books.employee')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='books.reader')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
