from django.db import models
from django.core.validators import MinValueValidator


class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'

GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)


DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Car(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    model = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=20)
    mileage = models.PositiveIntegerField()
    volume = models.FloatField(validators=[MinValueValidator(0.0)])
    body_type = models.CharField(max_length=20, choices=BODY_TYPE_CHOICES)
    drive_unitc = models.CharField(max_length=20, choices=DRIVE_UNIT_CHOICES)
    gearbox = models.CharField(max_length=20, choices=GEARBOX_CHOICES)
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPE_CHOICES)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    image = models.ImageField(upload_to='images',
                              default='images/car-question-mark.png')
    def __str__(self):
        return f'{self.model} id{self.id}'

class Sale(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='sold_to_client')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='sold_car')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.created_at}: {self.car} - {self.client}'
