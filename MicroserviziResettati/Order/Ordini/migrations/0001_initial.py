# Generated by Django 3.2.11 on 2022-01-20 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_book', models.IntegerField()),
                ('id_customer', models.IntegerField()),
            ],
        ),
    ]
