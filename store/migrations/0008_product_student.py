# Generated by Django 4.0.5 on 2022-06-26 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.student'),
        ),
    ]
