# Generated by Django 3.0.5 on 2020-04-04 05:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('easy_res_api', '0003_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.RemoveField(
            model_name='food',
            name='price',
        ),
        migrations.AddField(
            model_name='food',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='food',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]