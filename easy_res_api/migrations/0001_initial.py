# Generated by Django 3.0.5 on 2020-04-08 17:15

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='Email Address')),
                ('date_of_birth', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
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
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default='67.00', max_digits=7)),
                ('order_date', models.DateTimeField()),
                ('customers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easy_res_api.Customers')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('food_type', models.CharField(max_length=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easy_res_api.Restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='customers',
            name='food',
            field=models.ManyToManyField(to='easy_res_api.Food'),
        ),
    ]
