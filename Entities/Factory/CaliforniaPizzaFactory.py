from Entities.Pizza.Pizza import Pizza
from Entities.Pizza.FourCheese.CaliforniaPizzaFourCheese import CaliforniaPizzaFourCheese as FourCheese
from Entities.Pizza.Hawaianna.CaliforniaPizzaHawaiana import CaliforniaPizzaHawaiana as Hawaiana
from Entities.Pizza.Pepperoni.CaliforniaPizzaPepperoni import CaliforniaPizzaPepperoni as Pepperoni
from Entities.Factory.PizzaFactory import PizzaFactory

from Interfaces.PizzaFactory import PizzaFactory as PizzaFactoryInterface
class CaliforniaPizzaFactory(PizzaFactory, PizzaFactoryInterface):
    def __init__(self): super().__init__("California Pizza Factory")
    
    def createPizza(self, type)->Pizza:
        pizza = None
        if type == 'Hawaiana': pizza = Hawaiana()
        elif type == 'FourCheese': pizza = FourCheese()
        else: pizza = Pepperoni()
        return pizza