# Generated by Django 2.1.7 on 2019-02-21 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_auto_20190220_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='price',
        ),
        migrations.AddField(
            model_name='pizza',
            name='s_price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pizza',
            name='l_price',
            field=models.FloatField(default=0),
            preserve_default=False,
        )
    ]
