# Generated by Django 3.2.11 on 2022-01-20 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titolo', models.CharField(max_length=50)),
                ('Autore', models.CharField(max_length=50)),
                ('DAta_pubblicazione', models.DateTimeField(verbose_name='date published')),
                ('Prezzo', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
