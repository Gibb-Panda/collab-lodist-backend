# Generated by Django 5.0.4 on 2024-05-19 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("logistic", "0008_alter_commodity_good_hazard_class"),
    ]

    operations = [
        migrations.RenameField(
            model_name="commodity",
            old_name="packagin_information",
            new_name="packaging_information",
        ),
        migrations.AddField(
            model_name="storagecondition",
            name="warehouse",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="storage_conditions",
                to="logistic.warehouse",
            ),
        ),
    ]