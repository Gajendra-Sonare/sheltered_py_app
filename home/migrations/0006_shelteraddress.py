# Generated by Django 3.1.6 on 2022-06-21 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20220621_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShelterAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landmark', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
                ('pincode', models.IntegerField(verbose_name=6)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.publicpost')),
            ],
        ),
    ]