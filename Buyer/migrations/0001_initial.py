# Generated by Django 2.2.1 on 2020-03-01 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Seller', '0009_goods_goods_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=32, unique=True, verbose_name='订单编号')),
                ('order_date', models.DateField(auto_now=True, verbose_name='订单创建时间')),
                ('order_status', models.IntegerField(choices=[(1, '未支付'), (2, '已支付'), (3, '待发货'), (4, '已发货'), (5, '拒收'), (6, '已完成')], verbose_name='订单状态')),
                ('order_total', models.FloatField(verbose_name='订单总价')),
                ('order_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller.LoginUser')),
            ],
            options={
                'db_table': 'payorder',
            },
        ),
        migrations.CreateModel(
            name='OrderInofo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_price', models.FloatField(verbose_name='商品的单价')),
                ('goods_count', models.IntegerField(verbose_name='购买的单品的数量')),
                ('goods_total_price', models.FloatField(verbose_name='购买的单品总金额')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller.Goods')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Buyer.PayOrder')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller.LoginUser', verbose_name='卖家')),
            ],
            options={
                'db_table': 'orderinfo',
            },
        ),
    ]
