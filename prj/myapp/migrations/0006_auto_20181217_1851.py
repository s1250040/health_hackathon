# Generated by Django 2.1.3 on 2018-12-17 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20181217_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alcohol',
            name='number',
        ),
        migrations.AlterField(
            model_name='alcohol',
            name='degree',
            field=models.IntegerField(choices=[('', '度数を選択してください。'), (3, '3%'), (4, '4%'), (5, '5%'), (6, '6%'), (7, '7%'), (8, '8%'), (10, '10%'), (12, '12%'), (14, '14%'), (15, '15%'), (17, '17%'), (20, '20%'), (25, '25%'), (30, '30%'), (35, '35%'), (40, '40%'), (45, '45%')], default=0),
        ),
        migrations.AlterField(
            model_name='alcohol',
            name='value',
            field=models.IntegerField(choices=[('', '量(サイズ)を選択してください。'), (180, '180ml(1合分)'), (200, '200ml(コップ1杯分)'), (350, '350ml(通常の1缶分)'), (500, '500ml(縦長の1缶分)'), (750, '750ml(4合瓶)'), (1800, '1800ml(1小瓶)')], default=0),
        ),
    ]
