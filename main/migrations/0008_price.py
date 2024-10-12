# Generated by Django 4.2.15 on 2024-10-10 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_review_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=200)),
                ('country_city', models.CharField(max_length=200)),
                ('price_range_start', models.CharField(max_length=10)),
                ('price_range_end', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='price')),
            ],
        ),
    ]
