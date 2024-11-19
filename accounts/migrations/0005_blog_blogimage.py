# Generated by Django 5.1.2 on 2024-10-25 16:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_product_options_categoryimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('slug', models.SlugField(max_length=150, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Photo')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.blog')),
            ],
        ),
    ]
