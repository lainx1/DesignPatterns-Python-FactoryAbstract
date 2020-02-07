from Entities.Pizza.Pizza import Pizza
from Interfaces.Pizza import Pizza as PizzaFactory
 
class MXPizzaHawaiana(Pizza, PizzaFactory):
    def __init__(self): super().__init__("MX Pizza Hawaiana")

    def cut(self): print(f'Cut for - {self}')
    def box(self): print(f'Box for - {self}')
    def prepare(self): print(f'Prepare for - {self}')
    def bake(self): print(f'Backe for - {self}')