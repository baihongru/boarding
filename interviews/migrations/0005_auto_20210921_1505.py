# Generated by Django 3.2.6 on 2021-09-21 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0004_alter_candidate_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='first_result',
            field=models.CharField(blank=True, choices=[('PASS', '通过'), ('UNDETERMINED', '待定'), ('DROP', '放弃')], max_length=100, verbose_name='一面结果'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='second_result',
            field=models.CharField(blank=True, choices=[('PASS', '通过'), ('UNDETERMINED', '待定'), ('DROP', '放弃')], max_length=100, verbose_name='二面结果'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='third_result',
            field=models.CharField(blank=True, choices=[('PASS', '通过'), ('UNDETERMINED', '待定'), ('DROP', '放弃')], max_length=100, verbose_name='三面结果'),
        ),
    ]
