# Generated by Django 3.0.1 on 2022-02-23 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_id', models.IntegerField()),
                ('to_id', models.IntegerField()),
                ('payment', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
    ]
