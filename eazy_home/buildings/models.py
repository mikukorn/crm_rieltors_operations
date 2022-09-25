from django.db import models

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
    time_update = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.id


class Flat_table(models.Model):
    PROMO = 'promo'
    LIVING = 'living'
    NONLIVING = 'non-living'
    TYPE = [
        (PROMO, "Промо объект"),
        (LIVING, "Жилое"),
        (NONLIVING, "Не жилое"),
    ]
    flat_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    number = models.CharField(max_length=255, verbose_name="Номер квартиры")
    entrance = models.IntegerField(verbose_name="Подъезд")
    floor = models.IntegerField(verbose_name="Этаж")
    area = models.CharField(max_length=255, verbose_name="Площадь")
    live_area = models.CharField(max_length=255, verbose_name="Жилая площадь", null=True)
    room_count = models.IntegerField(verbose_name="Кол-во комнат")
    price = models.CharField(max_length=255, verbose_name="Цена")
    type_object = models.CharField(max_length=32, choices=TYPE, default=LIVING, verbose_name="Тип объекта")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now_add=True, verbose_name="Дата обновления")
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return self.flat_id



