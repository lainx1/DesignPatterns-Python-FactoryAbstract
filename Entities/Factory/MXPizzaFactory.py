from Entities.Factory.PizzaFactory import PizzaFactory
from Interfaces.PizzaFactory import PizzaFactory as PizzaFactoryInterface
from Entities.Pizza.Pizza import Pizza
from Entities.Pizza.FourCheese.MXPizzaFourCheese import MXPizzaFourCheese as FourCheese
from Entities.Pizza.Hawaianna.MXPizzaHawaiana import MXPizzaHawaiana as Hawaiana
from Entities.Pizza.Pepperoni.MXPizzaPepperoni import MXPizzaPepperoni as Pepperoni

class MXPizzaFactory(PizzaFactory, PizzaFactoryInterface):
    def __init__(self): super().__init__("MX Pizza Factory")

    def createPizza(self, type)->Pizza:
        pizza = None
        if type == 'Hawaiana': pizza = Hawaiana()
        elif type == 'FourCheese': pizza = FourCheese()
        else: pizza = Pepperoni()
        return pizza
    