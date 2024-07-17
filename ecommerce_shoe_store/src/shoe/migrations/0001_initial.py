# Generated by Django 5.0.6 on 2024-07-17 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image_url', models.CharField(null=True)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=300, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='category.category')),
            ],
            options={
                'db_table': 'shoe',
            },
        ),
        migrations.CreateModel(
            name='ShoeSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoe.shoe')),
            ],
            options={
                'db_table': 'shoe_size',
            },
        ),
    ]
