from Entities.Pizza.Pizza import Pizza
from Interfaces.Pizza import Pizza as PizzaInterface

class NYPizzaFourCheese(Pizza, PizzaInterface):
    def __init__(self): super().__init__('NY Four Cheese')

    def cut(self): print(f'Cut for - {self}')
    def box(self): print(f'Box for - {self}')
    def prepare(self): print(f'Prepare for - {self}')
    def bake(self): print(f'Backe for - {self}')