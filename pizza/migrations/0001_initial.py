# Generated by Django 2.1.7 on 2019-02-20 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('o_type', models.CharField(max_length=64)),
                ('size', models.CharField(max_length=64)),
                ('extras', models.CharField(max_length=512)),
                ('price', models.IntegerField()),
                ('owner', models.CharField(max_length=64)),
                ('status', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('p_class', models.CharField(max_length=64)),
                ('num_extras', models.IntegerField()),
                ('size', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
