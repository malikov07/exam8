# Generated by Django 5.0.3 on 2024-06-18 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_order_products_delete_orderproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60)),
                ('username', models.CharField(max_length=60, null=True, unique=True)),
                ('telegram_id', models.PositiveBigIntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
