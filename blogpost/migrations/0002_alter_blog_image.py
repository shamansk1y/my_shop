# Generated by Django 4.1.7 on 2023-04-02 15:42

from django.db import migrations, models
import main_page.utils


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=None, upload_to=main_page.utils.get_file_name_id),
            preserve_default=False,
        ),
    ]
