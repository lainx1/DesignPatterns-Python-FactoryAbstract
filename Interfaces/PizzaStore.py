from abc import ABC, abstractmethod
from Entities.Pizza.Pizza import Pizza
class PizzaStore(ABC):

    @abstractmethod
    def orderPizza(self, type)->Pizza: raise NotImplementedError
    @abstractmethod
    def createPizza(self, type)->Pizza: raise NotImplementedError