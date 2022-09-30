from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Building(models.Model):
    PROMO = 'promo'
    LIVING = 'living'
    NONLIVING = 'non-living'
    TYPE = [
        (PROMO, "Промо объект"),
        (LIVING,  "Жилое"),
        (NONLIVING, "Не жилое"),
    ]

    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    number = models.CharField(max_length=255, verbose_name="Номер дома")
    street = models.CharField(max_length=255, verbose_name="Улица")
    city = models.CharField(max_length=255, verbose_name="Город")
    type_object = models.CharField(max_length=32, choices=TYPE, default=LIVING, verbose_name="Тип объекта")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now_add=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.id

class Employeers(models.Model):
    MANAGER = 'manager'
    REALTOR = 'realtor'
    TYPE = [
        (MANAGER, "Менеджер"),
        (REALTOR, "Риэлтор"),
    ]
    id_employeer = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id_employeer')
    firstname = models.CharField(max_length=255, verbose_name="Имя")
    lastname = models.CharField(max_length=255, verbose_name="Фамилия")
    email = models.CharField(max_length=255, verbose_name="Email")
    phonenumber = PhoneNumberField(blank=True, verbose_name="Номер телефона")
    role = models.CharField(max_length=32, choices=TYPE, default=REALTOR, verbose_name="Роль")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now_add=True, verbose_name="Дата обновления")

class Deal(models.Model):
    R = 'Request'
    CN = 'Clarification needed'
    IW = 'In work'
    UR = 'Under review'
    CMPLTD = 'Completed'
    CNCLD = 'Canceled'
    ARCH = 'Archived'
    STATUS_TYPE = [
        (R, "Запрос сделки"),
        (CN, "Нужно уточнение"),
        (IW, "В работе"),
        (UR, "Ревью"),
        (CMPLTD, "Завершена"),
        (CNCLD, "Отменена"),
        (ARCH, "Archived"),
    ]
    RENT = 'Rent'
    SALE = 'Sale'
    PURCHASE = 'Purchase'
    DEAL_TYPE = [
        (RENT, "Аренда"),
        (SALE, "Продажа"),
        (PURCHASE, "Купля"),
    ]

    id_deal = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id_deal')
    id_status_deal = models.CharField(max_length=32, choices=STATUS_TYPE, default=R, verbose_name="Статус сделки")
    id_type_deal = models.CharField(max_length=32, choices=DEAL_TYPE, default=R, verbose_name="Тип сделки")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now_add=True, verbose_name="Дата обновления")


class Contract(models.Model):
    id_contract = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id_contract')
    contractnumber = models.CharField(max_length=255, verbose_name="Номер договора")
    description = models.CharField(max_length=255, verbose_name="Описание", null=True)
    sum = models.CharField(max_length=255, verbose_name="Сумма", null=True)
    id_deal = models.ForeignKey(Deal, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now_add=True, verbose_name="Дата обновления")

class Client(models.Model):
    id_client = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id_client')
    firstname = models.CharField(max_length=255, verbose_name="Имя")
    lastname = models.CharField(max_length=255, verbose_name="Фамилия")
    email = models.CharField(max_length=255, verbose_name="Email")
    phonenumber = PhoneNumberField(blank=True, verbose_name="Номер телефона")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now_add=True, verbose_name="Дата обновления")

class Estate(models.Model):
    LIVING = 'Жилое'
    NONLIVING = 'Не жилое'
    TYPE = [
        (LIVING, "Жилое"),
        (NONLIVING, "Не жилое"),
    ]
    id_estate = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id_estate')
    address = models.CharField(max_length=255, verbose_name="Адрес")
    active = models.BooleanField(verbose_name='Is active?', null=True)
    type_object = models.CharField(max_length=32, choices=TYPE, default=LIVING, verbose_name="Тип объекта")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now_add=True, verbose_name="Дата обновления")

class Estate_client(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')
    active = models.BooleanField(verbose_name='Is active?', null=True)
    id_estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    id_deal = models.ForeignKey(Deal, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now_add=True, verbose_name="Дата обновления")




