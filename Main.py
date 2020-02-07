from Entities.Store.NYPizzaStore import NYPizzaStore
from Entities.Store.MXPizzaStore import MXPizzaStore
from Entities.Store.CaliforniaPizzaStore import CaliforniaPizzaStore

from Entities.Factory.NYPizzaFactory import NYPizzaFactory
from Entities.Factory.MXPizzaFactory import MXPizzaFactory
from Entities.Factory.CaliforniaPizzaFactory import CaliforniaPizzaFactory

print('****************************************************************************************')
nyPizzaStore = NYPizzaStore(NYPizzaFactory())
nypizza = nyPizzaStore.orderPizza('Hawaiana')
print(nypizza)
print('****************************************************************************************')
mxPizzaStore = MXPizzaStore(MXPizzaFactory())
mxPizza = mxPizzaStore.orderPizza('Pepperoni')
print(mxPizza)
print('****************************************************************************************')
californiaPizzaStore = CaliforniaPizzaStore(CaliforniaPizzaFactory())
californiaPizza = californiaPizzaStore.orderPizza('FourCheese')
print(californiaPizza)