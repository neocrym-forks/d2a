# Generated by Django 2.0 on 2018-01-11 17:10

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
                'db_table': 'mysql_author',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('content', models.BinaryField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='mysql_app.Author')),
            ],
            options={
                'db_table': 'mysql_book',
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
                'db_table': 'mysql_category',
            },
        ),
        migrations.CreateModel(
            name='CategoryRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30, null=True)),
                ('category1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='mysql_app.Category')),
                ('category2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='mysql_app.Category')),
            ],
            options={
                'db_table': 'mysql_category_relation',
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('sold', models.DateTimeField(auto_now_add=True)),
                ('reservation', models.DurationField(null=True)),
                ('source', models.GenericIPAddressField(null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='mysql_app.Book')),
            ],
            options={
                'db_table': 'mysql_sales',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='related_coming',
            field=models.ManyToManyField(related_name='related_going', through='mysql_app.CategoryRelation', to='mysql_app.Category'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(related_name='books', to='mysql_app.Category'),
        ),
    ]
