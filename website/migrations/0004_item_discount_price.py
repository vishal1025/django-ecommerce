# Generated by Django 2.2.5 on 2019-10-28 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
