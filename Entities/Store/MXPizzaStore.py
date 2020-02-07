from Entities.Pizza.Pizza import Pizza
from Entities.Store.PizzaStore import PizzaStore
from Entities.Factory.MXPizzaFactory import MXPizzaFactory
from Interfaces.PizzaStore import PizzaStore as PizzaStoreInterface

class MXPizzaStore(PizzaStore, PizzaStoreInterface):
    def __init__(self, mxPizzaFactory): 
        super().__init__("MX Pizza Store")
        self._mxPizzaFactory = mxPizzaFactory
    @property
    def mxPizzaFactory(self): return self._mxPizzaFactory
    @mxPizzaFactory.setter
    def mxPizzaFactory(self, mxPizzaFactory): self._mxPizzaFactory = mxPizzaFactory
    
    def orderPizza(self, type)->Pizza:
        pizza = self.createPizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
    
    def createPizza(self, type)->Pizza:
        return self.mxPizzaFactory.createPizza(type)