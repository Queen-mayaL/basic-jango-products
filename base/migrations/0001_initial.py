# Generated by Django 5.2 on 2025-04-22 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('stock_quantity', models.IntegerField()),
                ('category_id', models.IntegerField()),
                ('supplier_id', models.IntegerField()),
            ],
            options={
                'db_table': 'base_product',
            },
        ),
    ]
