# Generated by Django 2.0.7 on 2018-07-03 13:57

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('price', django.contrib.postgres.fields.jsonb.JSONField()),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('content', models.BinaryField()),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), size=3)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='books.Author')),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='CategoryRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30, null=True)),
                ('category1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='books.Category')),
                ('category2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='books.Category')),
            ],
            options={
                'db_table': 'category_relation',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='related_coming',
            field=models.ManyToManyField(related_name='related_going', through='books.CategoryRelation', to='books.Category'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(related_name='books', to='books.Category'),
        ),
    ]
