from Interfaces.PizzaFactory import PizzaFactory as PizzaInterface
from Entities.Factory.PizzaFactory import PizzaFactory
from Entities.Pizza.Pizza import Pizza
from Entities.Pizza.Hawaianna.NYPizzaHawaiana import NYPizzaHawaiana as Hawaiana
from Entities.Pizza.FourCheese.NYPizzaFourCheese import NYPizzaFourCheese as FourCheese
from Entities.Pizza.Pepperoni.NYPizzaPepperoni import NYPizzaPepperoni as Pepperoni

class NYPizzaFactory(PizzaFactory, PizzaInterface):
    def __init__(self): super().__init__('NYPizzaFactory')

    def createPizza(self, type)->Pizza:
        pizza = None
        if type == 'Hawaiana': pizza = Hawaiana()
        elif type == 'FourCheese': pizza = FourCheese()
        else: pizza = Pepperoni()
        return pizza