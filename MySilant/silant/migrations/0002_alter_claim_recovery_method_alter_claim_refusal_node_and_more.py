# Generated by Django 4.2.4 on 2023-08-04 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('silant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='recovery_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.recoverymethod'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='refusal_node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.refusalnode'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='service_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.servicecompany'),
        ),
        migrations.AlterField(
            model_name='client',
            name='description',
            field=models.CharField(default='Клиент', max_length=255),
        ),
        migrations.AlterField(
            model_name='drivingaxle',
            name='description',
            field=models.CharField(default='Модель ведущего моста', max_length=255),
        ),
        migrations.AlterField(
            model_name='engine',
            name='description',
            field=models.CharField(default='Модель двигателя', max_length=255),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='description',
            field=models.CharField(default='Модель техники', max_length=255),
        ),
        migrations.AlterField(
            model_name='machine',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.client'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='model_driving_axle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.drivingaxle'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='model_engine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.engine'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='model_equipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.equipment'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='model_steering_axle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.steeringaxle'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='model_transmission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.transmission'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='service_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.servicecompany'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='maintenance_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.maintenancecompany'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='service_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.servicecompany'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.typemaintenance'),
        ),
        migrations.AlterField(
            model_name='maintenancecompany',
            name='description',
            field=models.CharField(default='Организация выполняющая ТО', max_length=255),
        ),
        migrations.AlterField(
            model_name='recoverymethod',
            name='description',
            field=models.CharField(default='Способ восстановления', max_length=255),
        ),
        migrations.AlterField(
            model_name='refusalnode',
            name='description',
            field=models.CharField(default='Узел отказа', max_length=255),
        ),
        migrations.AlterField(
            model_name='servicecompany',
            name='description',
            field=models.CharField(default='Сервисная компания', max_length=255),
        ),
        migrations.AlterField(
            model_name='steeringaxle',
            name='description',
            field=models.CharField(default='Модель управляемого моста', max_length=255),
        ),
        migrations.AlterField(
            model_name='transmission',
            name='description',
            field=models.CharField(default='Модель трансмиссии', max_length=255),
        ),
        migrations.AlterField(
            model_name='typemaintenance',
            name='description',
            field=models.CharField(default='Вид технического обслуживания', max_length=255),
        ),
    ]
