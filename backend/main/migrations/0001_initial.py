# Generated by Django 3.0.2 on 2020-01-11 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('admn_no', models.CharField(max_length=8)),
                ('degree', models.CharField(max_length=10)),
                ('adress', models.CharField(max_length=500)),
                ('addhar', models.CharField(max_length=12)),
                ('ph_no', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
