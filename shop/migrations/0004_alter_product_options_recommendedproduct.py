# Generated by Django 4.1.7 on 2023-03-12 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created',), 'verbose_name_plural': 'Товари'},
        ),
        migrations.CreateModel(
            name='RecommendedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
            options={
                'verbose_name_plural': 'Рекомендовані товари',
                'ordering': ['position'],
            },
        ),
    ]
