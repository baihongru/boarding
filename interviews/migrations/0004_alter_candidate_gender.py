# Generated by Django 3.2.6 on 2021-09-21 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0003_auto_20210921_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='gender',
            field=models.CharField(choices=[('MALE', '男'), ('FEMALE', '女'), ('OTHER', '其他')], max_length=100, verbose_name='性别'),
        ),
    ]