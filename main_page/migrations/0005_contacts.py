# Generated by Django 4.1.7 on 2023-03-11 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_advantages_alter_baner_image_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=70, verbose_name='Адреса')),
                ('phone_1', models.CharField(max_length=50, verbose_name='Телефон 1')),
                ('phone_2', models.CharField(max_length=50, verbose_name='Телефон 2')),
                ('phone_3', models.CharField(max_length=50, verbose_name='Телефон 3')),
                ('email', models.CharField(max_length=50, verbose_name='Пошта ')),
                ('day_open', models.CharField(max_length=50, verbose_name='Робочі дні')),
                ('hours_of_work', models.CharField(max_length=50, verbose_name='Робочі години')),
                ('weekend_work', models.CharField(max_length=50, verbose_name='Робота в вихідні')),
                ('weekend_hours_of_work', models.CharField(max_length=50, verbose_name='Робочі години в вихідні')),
                ('fb_url', models.URLField(blank=True, default='https://www.facebook.com/', verbose_name='Посилання на facebook')),
                ('youtube_url', models.URLField(blank=True, default='https://www.youtube.com/', verbose_name='Посилання на youtube')),
                ('in_url', models.URLField(blank=True, default='https://www.instagram.com/', verbose_name='Посилання на instagram')),
            ],
            options={
                'verbose_name_plural': 'Контакти',
                'ordering': ('address',),
            },
        ),
    ]
