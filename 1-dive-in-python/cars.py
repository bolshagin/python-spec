import os
import csv

from typing import List, Any


class CarBase:
    """Базовый класс для всех типов машин"""

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        try:
            self.carrying = float(carrying)
        except ValueError:
            self.carrying = 0.0

    def get_photo_file_ext(self) -> str:
        _, ext = os.path.splitext(self.photo_file_name)
        return ext


class Car(CarBase):
    car_type: str = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.passenger_seats_count = int(passenger_seats_count)
        except ValueError:
            self.passenger_seats_count = 0


class Truck(CarBase):
    car_type: str = 'truck'
    body_length: float = 0.0
    body_width: float = 0.0
    body_height: float = 0.0

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        if body_whl == '':
            body_whl = '0.0x0.0x0.0'
        self.body_whl = body_whl

        if body_whl:
            whl = body_whl.split('x')
            if len(whl) == 3:
                self.body_length = float(whl[0])
                self.body_width = float(whl[1])
                self.body_height = float(whl[2])

    def get_body_volume(self) -> float:
        return self.body_length * self.body_height * self.body_width


class SpecMachine(CarBase):
    car_type: str = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def check_row(row):
    photo_file_name = row['photo_file_name']
    carrying = row['carrying']
    passenger_seats_count = row['passenger_seats_count']
    brand = row['brand']
    extra = row['extra']
    car_type = row['car_type']

    exts = ['.jpg', '.jpeg', '.png', '.gif']
    ext = os.path.splitext(photo_file_name)[1]
    
    is_ok = True

    if photo_file_name.find('.') == -1 \
            or photo_file_name.rfind('.') == 0 \
            or photo_file_name == '.' \
            or ext not in exts:
        is_ok = False
    if not brand:
        is_ok = False
    if not extra and car_type == 'spec_machine':
        is_ok = False

    try:
        float(carrying)
        if car_type == 'car':
            int(passenger_seats_count)
    except ValueError:
        is_ok = False

    return is_ok


def get_car_list(csv_filename) -> List[Any]:
    car_list = []
    with open(csv_filename, encoding='utf-8') as f:
        cr = csv.DictReader(f, delimiter=';')
        for row in cr:
            if not row or not row['car_type'] or not check_row(row):
                continue
            obj = None
            if row['car_type'] == 'car':
                obj = Car(row['brand'], row['photo_file_name'], row['carrying'], row['passenger_seats_count'])
            elif row['car_type'] == 'truck':
                obj = Truck(row['brand'], row['photo_file_name'], row['carrying'], row['body_whl'])
            elif row['car_type'] == 'spec_machine':
                obj = SpecMachine(row['brand'], row['photo_file_name'], row['carrying'], row['extra'])
            else:
                continue
            car_list.append(obj)
    return car_list


if __name__ == '__main__':
    cars = get_car_list('coursera_week3_cars.csv')
    for car in cars:
        print(car.brand)
