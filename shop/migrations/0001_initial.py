# Generated by Django 3.2 on 2021-04-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=60)),
                ('desc', models.CharField(max_length=350)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
