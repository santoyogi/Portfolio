# Generated by Django 2.2 on 2023-06-20 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioDatabase', '0003_hobbies_hobby_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobbies',
            name='hobby_image',
            field=models.CharField(default='https://sarkissian.pro/wp-content/uploads/2021/01/Jewelry-Inventory-1-256x256.png', max_length=500),
        ),
    ]
