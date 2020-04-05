# Generated by Django 3.0.5 on 2020-04-05 03:03

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('easy_res_api', '0004_auto_20200404_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Sample customer', max_length=100)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(default='0887867346', max_length=128, region=None, unique=True)),
                ('email', models.EmailField(default='abc@gmail.xyz', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Sample Restaurant', max_length=100)),
                ('address', models.CharField(default='No 12, Abc street, centrel city,NY', max_length=250)),
                ('email', models.EmailField(default='abc@gmail.com', max_length=250)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(default='0717878782', max_length=128, region=None, unique=True)),
                ('latitude', models.DecimalField(decimal_places=16, default='90.12121121', max_digits=22)),
                ('longitude', models.DecimalField(decimal_places=16, default='90.12121121', max_digits=22)),
            ],
        ),
        migrations.RenameField(
            model_name='food',
            old_name='type',
            new_name='food_type',
        ),
        migrations.AddField(
            model_name='food',
            name='price',
            field=models.DecimalField(decimal_places=2, default=12.0, max_digits=7),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default='67.00', max_digits=7)),
                ('order_date', models.DateTimeField()),
                ('customers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easy_res_api.Customers')),
            ],
        ),
        migrations.AddField(
            model_name='customers',
            name='food',
            field=models.ManyToManyField(to='easy_res_api.Food'),
        ),
        migrations.AddField(
            model_name='food',
            name='restaurant',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='easy_res_api.Restaurant'),
            preserve_default=False,
        ),
    ]