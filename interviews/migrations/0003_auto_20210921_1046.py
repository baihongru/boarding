# Generated by Django 3.2.6 on 2021-09-21 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0002_auto_20210921_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='apply_position',
            field=models.CharField(max_length=100, verbose_name='应聘职位'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='gender',
            field=models.CharField(max_length=100, verbose_name='性别'),
        ),
    ]
