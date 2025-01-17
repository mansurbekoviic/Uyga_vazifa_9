# Generated by Django 5.0.6 on 2025-01-13 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
