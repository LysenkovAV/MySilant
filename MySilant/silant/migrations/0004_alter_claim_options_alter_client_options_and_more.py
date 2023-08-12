# Generated by Django 4.2.4 on 2023-08-07 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('silant', '0003_alter_machine_number_machine'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='claim',
            options={'verbose_name': 'Рекламация', 'verbose_name_plural': 'Рекламации'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='drivingaxle',
            options={'verbose_name': 'Модель ведущего моста', 'verbose_name_plural': 'Модели ведущих мостов'},
        ),
        migrations.AlterModelOptions(
            name='engine',
            options={'verbose_name': 'Модель двигателя', 'verbose_name_plural': 'Модели двигателей'},
        ),
        migrations.AlterModelOptions(
            name='equipment',
            options={'verbose_name': 'Модель техники', 'verbose_name_plural': 'Модели техники'},
        ),
        migrations.AlterModelOptions(
            name='machine',
            options={'verbose_name': 'Машина', 'verbose_name_plural': 'Машины'},
        ),
        migrations.AlterModelOptions(
            name='maintenance',
            options={'verbose_name': 'Техническое обслуживание', 'verbose_name_plural': 'Технические обслуживания'},
        ),
        migrations.AlterModelOptions(
            name='maintenancecompany',
            options={'verbose_name': 'Организация, проводившая ТО', 'verbose_name_plural': 'Организации, проводившие ТО'},
        ),
        migrations.AlterModelOptions(
            name='recoverymethod',
            options={'verbose_name': 'Способ восстановления', 'verbose_name_plural': 'Способы восстановлений'},
        ),
        migrations.AlterModelOptions(
            name='refusalnode',
            options={'verbose_name': 'Узел отказа', 'verbose_name_plural': 'Узлы отказов'},
        ),
        migrations.AlterModelOptions(
            name='servicecompany',
            options={'verbose_name': 'Сервисная компания', 'verbose_name_plural': 'Сервисные компании'},
        ),
        migrations.AlterModelOptions(
            name='steeringaxle',
            options={'verbose_name': 'Модель управляемого моста', 'verbose_name_plural': 'Модели управляемых мостов'},
        ),
        migrations.AlterModelOptions(
            name='transmission',
            options={'verbose_name': 'Модель трансмиссии', 'verbose_name_plural': 'Модели трансмиссий'},
        ),
        migrations.AlterModelOptions(
            name='typemaintenance',
            options={'verbose_name': 'Вид технического обслуживания', 'verbose_name_plural': 'Виды технических обслуживаний'},
        ),
        migrations.AlterField(
            model_name='claim',
            name='downtime',
            field=models.IntegerField(default=0, verbose_name='Время простоя техники'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.machine', verbose_name='Машина'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='operating_time',
            field=models.IntegerField(default=0, verbose_name='Наработка, м/час'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='recovery_date',
            field=models.DateField(verbose_name='Дата восстановления'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='recovery_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.recoverymethod', verbose_name='Способ восстановления'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='refusal_date',
            field=models.DateField(verbose_name='Дата отказа'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='refusal_description',
            field=models.TextField(max_length=1000, verbose_name='Описание отказа'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='refusal_node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.refusalnode', verbose_name='Узел отказа'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='repair_parts',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Используемые запасные части'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='service_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.servicecompany', verbose_name='Сервисная компания'),
        ),
        migrations.AlterField(
            model_name='client',
            name='description',
            field=models.CharField(default='Клиент', max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='client',
            name='title',
            field=models.CharField(default='noname', max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='drivingaxle',
            name='description',
            field=models.CharField(default='Модель ведущего моста', max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='drivingaxle',
            name='title',
            field=models.CharField(default='noname', max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='engine',
            name='description',
            field=models.CharField(default='Модель двигателя', max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='engine',
            name='title',
            field=models.CharField(default='noname', max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='description',
            field=models.CharField(default='Модель техники', max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='title',
            field=models.CharField(default='noname', max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='end_consumer',
            field=models.CharField(max_length=255, verbose_name='Грузополучатель (конечный потребитель)'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='model_driving_axle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.drivingaxle', verbose_name='Модель ведущего моста'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='model_engine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.engine', verbose_name='Модель двигателя'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='model_equipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.equipment', verbose_name='Модель техники'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='model_steering_axle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.steeringaxle', verbose_name='Модель управляемого моста'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='model_transmission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.transmission', verbose_name='Модель трансмиссии'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='number_driving_axle',
            field=models.CharField(max_length=255, verbose_name='Заводской номер ведущего моста'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='number_engine',
            field=models.CharField(max_length=255, verbose_name='Заводской номер двигателя'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='number_machine',
            field=models.CharField(max_length=255, unique=True, verbose_name='Заводской номер машины'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='number_steering_axle',
            field=models.CharField(max_length=255, verbose_name='Заводской номер управляемого моста'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='number_transmission',
            field=models.CharField(max_length=255, verbose_name='Заводской номер трансмиссии'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='options',
            field=models.TextField(default='Стандарт', max_length=1000, verbose_name='Комплектация (дополнительные опции)'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='service_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.servicecompany', verbose_name='Сервисная компания'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='shipment_date',
            field=models.DateField(verbose_name='Дата отгрузки с завода'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='shipping_address',
            field=models.CharField(max_length=255, verbose_name='Адрес поставки (эксплуатации)'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='supply_contract',
            field=models.CharField(max_length=255, verbose_name='Договор поставки (номер, дата)'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.machine', verbose_name='Машина'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='maintenance_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.maintenancecompany', verbose_name='Организация, проводившая ТО'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='maintenance_date',
            field=models.DateField(verbose_name='Дата проведения ТО'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='operating_time',
            field=models.IntegerField(default=0, verbose_name='Наработка, м/час'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='order_date',
            field=models.DateField(verbose_name='Дата заказ-наряда'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='order_number',
            field=models.CharField(max_length=255, verbose_name='Номер заказ-наряда'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='service_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.servicecompany', verbose_name='Сервисная компания'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.typemaintenance', verbose_name='Вид ТО'),
        ),
        migrations.AlterField(
            model_name='maintenancecompany',
            name='description',
            field=models.CharField(default='Организация выполняющая ТО', max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='maintenancecompany',
            name='title',
            field=models.CharField(default='noname', max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='recoverymethod',
            name='description',
            field=models.CharField(default='Способ восстановления', max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='recoverymethod',
            name='title',
            field=models.CharField(default='noname', max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='refusalnode',
            name='description',
            field=models.CharField(default='Узел отказа', max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='refusalnode',
            name='title',
            field=models.CharField(default='noname', max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='servicecompany',
            name='description',
            field=models.CharField(default='Сервисная компания', max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='servicecompany',
            name='title',
            field=models.CharField(default='noname', max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='steeringaxle',
            name='description',
            field=models.CharField(default='Модель управляемого моста', max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='steeringaxle',
            name='title',
            field=models.CharField(default='noname', max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='transmission',
            name='description',
            field=models.CharField(default='Модель трансмиссии', max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='transmission',
            name='title',
            field=models.CharField(default='noname', max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='typemaintenance',
            name='description',
            field=models.CharField(default='Вид технического обслуживания', max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='typemaintenance',
            name='title',
            field=models.CharField(default='noname', max_length=255, verbose_name='Название'),
        ),
    ]