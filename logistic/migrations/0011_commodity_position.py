# Generated by Django 5.0.4 on 2024-05-24 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("logistic", "0010_commodity_warehouse"),
    ]

    operations = [
        migrations.AddField(
            model_name="commodity",
            name="position",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
