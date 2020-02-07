from abc import abstractmethod, ABC
from Entities.Pizza.Pizza import Pizza
class PizzaFactory(ABC):
    @abstractmethod
    def createPizza(self, type)->Pizza:
        raise NotImplementedError