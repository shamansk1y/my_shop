# Generated by Django 4.1.7 on 2023-03-27 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_orderitem_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='is_processed',
            field=models.BooleanField(default=False),
        ),
    ]
