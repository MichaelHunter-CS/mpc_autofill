# Generated by Django 3.2.3 on 2021-05-25 12:43

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cardpicker", "0012_auto_20210518_2352"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="searchq",
            field=django.contrib.postgres.search.SearchVectorField(),
        ),
        migrations.AlterField(
            model_name="cardback",
            name="searchq",
            field=django.contrib.postgres.search.SearchVectorField(),
        ),
        migrations.AlterField(
            model_name="token",
            name="searchq",
            field=django.contrib.postgres.search.SearchVectorField(),
        ),
        migrations.AddIndex(
            model_name="card",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["searchq"], name="cardpicker__searchq_3a5fec_gin"
            ),
        ),
        migrations.AddIndex(
            model_name="cardback",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["searchq"], name="cardpicker__searchq_f3fbbd_gin"
            ),
        ),
        migrations.AddIndex(
            model_name="token",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["searchq"], name="cardpicker__searchq_d72ef1_gin"
            ),
        ),
    ]