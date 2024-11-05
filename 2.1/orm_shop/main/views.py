from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse

from main.models import Car, Sale, Client

# список авто
def cars_list_view(request):
    template_name = 'main/list.html'
    context = {'cars':Car.objects.all()}
    return render(request, template_name, context)

# конкретная модель авто
def car_details_view(request, car_id):
    try:
        template_name = 'main/details.html'
        return render(request, template_name,
                      context = {'car':Car.objects.get(id=car_id)})
    except Car.DoesNotExist:
        raise Http404('Car not found')

# модель авто и её продажи
def sales_by_car(request, car_id):
    try:
        template_name = 'main/sales.html'
        context = {'car':Car.objects.get(id=car_id),
                   'sales':Sale.objects.filter(car=car_id)}
        return render(request, template_name, context)
    except Car.DoesNotExist:
        raise Http404('Car not found')

# Создание записей в таблицах (или их замена на дефолтные)
def recreate_tables(request):
    try:
        cars = [
            Car(id = 1, model = 'Жигули', year = 1990, color = 'Серо-буро-малиновый', mileage = '10000', volume = 1.2, body_type = 'Седан', drive_unitc = 'Задний', gearbox = 'Механика', fuel_type = 'Бензин', price = 300000.99, image = 'images/jiguli.png'),
            Car(id = 2, model = 'TESLA 2030 (предзаказ)', year = 2030, color = 'Белый', mileage = '0', volume = 0, body_type = 'Седан', drive_unitc = 'Полный', gearbox = 'Робот', fuel_type = 'Электро', price = 99999999.99),
            Car(id = 3, model = 'BMW X7', year = 2020, color = 'Синий', mileage = '0', volume = 3.0, body_type = 'Внедорожник', drive_unitc = 'Полный', gearbox = 'Автомат', fuel_type = 'Бензин', price = 6000000.00, image = 'images/bmw_x7.jpg'),
            Car(id = 4, model = 'Geely Monjaro', year = 2022, color = 'Синий', mileage = '0', volume = 3.0, body_type = 'Седан', drive_unitc = 'Полный', gearbox = 'Автомат', fuel_type = 'Бензин', price = 5000000.00, image = 'images/geely_monjaro.jpg'),
            Car(id = 5, model = 'Geländewagen', year = 2020, color = 'Серебристый', mileage = '500', volume = 5.0, body_type = 'Внедорожник', drive_unitc = 'Полный', gearbox = 'Автомат', fuel_type = 'Гибрид', price = 6000000.00, image = 'images/gelandewagen.jpg'),
            Car(id = 6, model = 'Volvo XC90', year = 2010, color = 'Баклажановый', mileage = '1000', volume = 3.2, body_type = 'Седан', drive_unitc = 'Полный', gearbox = 'Автомат', fuel_type = 'Бензин', price = 2000000.00, image = 'images/volvo_xc90.jpg')
        ]
        Car.objects.all().delete()
        Car.objects.bulk_create(cars)
        Client.objects.all().delete()
        client1 = Client(name = 'Иван', last_name = 'Иванов', middle_name = 'Иванович', date_of_birth = '2001-11-30', phone_number = '88008888888')
        client2 = Client(name = 'Петр', last_name = 'Петров', middle_name = 'Петрович', date_of_birth = '1995-05-15', phone_number = '85005555555')
        client3 = Client(name = 'Мария', last_name = 'Петровна', middle_name = 'Ивановна', date_of_birth = '1980-08-08', phone_number = '+7 700 777 77 77')
        client1.save()
        client2.save()
        client3.save()
        sales = [
            Sale(id = 1, client = client1, car = Car.objects.get(id=1)),
            Sale(id = 2, client = client1, car = Car.objects.get(id=2)),
            Sale(id = 3, client = client2, car = Car.objects.get(id=2)),
            Sale(id = 4, client = client3, car = Car.objects.get(id=3)),
            Sale(id = 5, client = client3, car = Car.objects.get(id=3)),
            Sale(id = 6, client = client3, car = Car.objects.get(id=5))
        ]
        Sale.objects.all().delete()
        Sale.objects.bulk_create(sales)
        return HttpResponse('Данные в БД сброшены до первоначальных значений')
    except:
        return HttpResponse('Ошибка')