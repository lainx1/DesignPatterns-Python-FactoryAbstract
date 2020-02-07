from Interfaces.Pizza import Pizza as PizzaInterface
from Entities.Pizza.Pizza import Pizza

class NYPizzaHawaiana(PizzaInterface, Pizza):

    def __init__(self): super().__init__("NY Hawaianna")
    
    def cut(self): print(f'Cut for - {self}')
    def box(self): print(f'Box for - {self}')
    def prepare(self): print(f'Prepare for - {self}')
    def bake(self): print(f'Backe for - {self}')