from Entities.Pizza.Pizza import Pizza
from Entities.Store.PizzaStore import PizzaStore
from Entities.Factory.NYPizzaFactory import NYPizzaFactory
from Interfaces.PizzaStore import PizzaStore as PizzaStoreInterface

class NYPizzaStore(PizzaStore, PizzaStoreInterface):
    def __init__(self, nyPizzaFactory): 
        super().__init__("NY Pizza Store")
        self._nyPizzaFactory = nyPizzaFactory
    @property
    def nyPizzaFactory(self): return self._nyPizzaFactory
    @nyPizzaFactory.setter
    def nyPizzaFactory(self, nyPizzaFactory): self._nyPizzaFactory = nyPizzaFactory

    def orderPizza(self, type)->Pizza:
        pizza = self.createPizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    def createPizza(self, type)->Pizza:
        return self.nyPizzaFactory.createPizza(type)
        
