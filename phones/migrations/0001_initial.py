# Generated by Django 3.1.2 on 2024-08-04 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('image', models.CharField(max_length=100)),
                ('release_date', models.CharField(max_length=50)),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
    ]
