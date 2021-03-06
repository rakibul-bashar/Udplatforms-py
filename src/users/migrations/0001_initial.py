# Generated by Django 3.1 on 2020-08-21 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('createdatupdatedatbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.createdatupdatedatbasemodel')),
                ('street', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zip_code', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
            bases=('common.createdatupdatedatbasemodel',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('createdatupdatedatbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.createdatupdatedatbasemodel')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('user_type', models.CharField(choices=[('PARENT', 'Parent'), ('CHILD', 'Child')], max_length=6)),
                ('addresses', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='users_address', to='users.address')),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
            bases=('common.createdatupdatedatbasemodel',),
        ),
    ]
