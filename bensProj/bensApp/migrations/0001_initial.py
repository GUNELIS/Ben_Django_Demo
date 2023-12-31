# Generated by Django 4.2.4 on 2023-09-02 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('account_managers', models.ManyToManyField(related_name='customers', to='bensApp.accountmanager')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('account_managers', models.ManyToManyField(related_name='service_providers', to='bensApp.accountmanager')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('service_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bensApp.serviceprovider')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('account_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bensApp.accountmanager')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bensApp.customer')),
                ('service', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bensApp.service')),
                ('service_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bensApp.serviceprovider')),
            ],
        ),
    ]
