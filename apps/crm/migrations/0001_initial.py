# Generated by Django 3.1.4 on 2020-12-08 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Company name')),
                ('country', models.CharField(max_length=25, verbose_name='Company country')),
                ('foundation_date', models.DateField(verbose_name='Company foundation date')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Position title')),
            ],
            options={
                'verbose_name': 'Position',
                'verbose_name_plural': 'Positions',
            },
        ),
        migrations.CreateModel(
            name='Partnership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='crm.company', verbose_name='Company')),
                ('partner', models.ManyToManyField(related_name='company_partner', to='crm.Company', verbose_name='Company-partner')),
            ],
            options={
                'verbose_name': 'Partnership',
                'verbose_name_plural': 'Partnerships',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Employee name')),
                ('surname', models.CharField(max_length=25, verbose_name='Employee surname')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6)),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Employee date of birth')),
                ('country', models.CharField(max_length=25, verbose_name='Employee country')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Employee email')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Employee biography')),
                ('employee_photo', models.ImageField(blank=True, null=True, upload_to='employees', verbose_name='Employee photo')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_company', to='crm.company', verbose_name='Employee company')),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_position', to='crm.position', verbose_name='Employee position')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
    ]
