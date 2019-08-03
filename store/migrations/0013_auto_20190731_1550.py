# Generated by Django 2.2.3 on 2019-07-31 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20190626_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoneyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('exchangeRate', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Принят в обработку', 'Принят в обработку'), ('Выполнен', 'Выполнен')], default='Принят в обработку', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='НАПИШИТЕ ОПИСАНИЕ ПРОДУКТА!'),
        ),
        migrations.AddField(
            model_name='product',
            name='money',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.MoneyType'),
            preserve_default=False,
        ),
    ]
