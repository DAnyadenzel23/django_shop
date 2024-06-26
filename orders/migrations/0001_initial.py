# Generated by Django 4.2.2 on 2024-01-20 18:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('indexapp', '0002_remove_sections_slug_alter_sections_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=25)),
                ('name_of_organization', models.CharField(max_length=25)),
                ('tin', models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(10)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('phone_number', models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(11)])),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexapp.products')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexapp.sections')),
            ],
        ),
    ]
