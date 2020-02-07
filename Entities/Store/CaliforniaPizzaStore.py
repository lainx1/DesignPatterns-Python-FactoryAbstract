from Entities.Pizza.Pizza import Pizza
from Entities.Factory.CaliforniaPizzaFactory import CaliforniaPizzaFactory
from Entities.Store.PizzaStore import PizzaStore

from Interfaces.PizzaStore import PizzaStore as PizzaStoreInterface

class CaliforniaPizzaStore(PizzaStore, PizzaStoreInterface):
    def __init__(self, californiaPizzaFactory): 
        super().__init__("California Pizza Store")
        self._californiaPizzaFactory = californiaPizzaFactory
        
    @property
    def californiaPizzaFactory(self): return self._californiaPizzaFactory
    @californiaPizzaFactory.setter
    def californiaPizzaFactory(self, californiaPizzaFactory): self._californiaPizzaFactory = californiaPizzaFactory
    
    def orderPizza(self, type)->Pizza:
        pizza = self.createPizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
    
    def createPizza(self, type)->Pizza:
        return self.californiaPizzaFactory.createPizza(type)