# Generated by Django 4.0.5 on 2022-06-26 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_product_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='student',
            field=models.ForeignKey(default=18, on_delete=django.db.models.deletion.CASCADE, to='store.student'),
        ),
    ]
