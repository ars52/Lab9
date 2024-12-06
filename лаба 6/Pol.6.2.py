class Vehicle:
    def __init__(self, make:str, model:str):
        self.make = make
        self.model = model

    def get_info(self) -> str:
        return (f'Марка: {self.make}, Модель: {self.model}')
    
class Car(Vehicle):

    def __init__(self, make:str, model:str, fuel_type:str):
        super().__init__(make,model)
        self.fuel_type = fuel_type

    def get_info(self) -> str:
        return f'{super().get_info()}, Тип топлива: {self.fuel_type}'
        


vehicle = Vehicle('Toyota','Camry')  
car = Car('Toyota','Corrola','Дизель')     
print(vehicle.get_info())
print(car.get_info())

