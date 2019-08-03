# Generated by Django 2.2.1 on 2019-05-24 22:07

from django.db import migrations, models
import django.db.models.deletion
import store.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ParentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True)),
                ('description', models.TextField(default='НАПИШИТЕ ОПИСАНИЕ ПРОДУКТА!')),
                ('image', models.ImageField(blank=True, upload_to=store.models.image_folder)),
                ('warranty', models.DecimalField(decimal_places=0, default=0, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('avaliable', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='store.Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Category')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='parentCategory',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.ParentCategory'),
        ),
    ]