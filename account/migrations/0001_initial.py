<<<<<<< HEAD
# Generated by Django 4.1.7 on 2023-04-02 14:22
=======
# Generated by Django 4.1.7 on 2023-03-29 17:34
>>>>>>> f54e6daafcc4fe9a70b2717eb1659f61a822a314

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
<<<<<<< HEAD
        ('shop', '0001_initial'),
=======
        ('shop', '0024_alter_product_characteristics_gender'),
>>>>>>> f54e6daafcc4fe9a70b2717eb1659f61a822a314
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
