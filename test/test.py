# ********************** Multi polymorphisme ********************** #

class classe_two:
# {
    def function_two():
        print("I am classe_two")
# }

class classe_tree:
# {
    def function_tree():
        print("I am classe_tree !!!")
    def function_Banane():
        print("I am Function_Banane in class tree !!!")
# }

class classe_one(classe_two, classe_tree):
# {
    def function_one(string: str):
        print(string)
# }

cla_one: classe_one = classe_one
cla_one.function_one("AAAAAA")
cla_one.function_two()
cla_one.function_tree()
cla_one.function_Banane()

# ********************** Fonction Template ********************** #
from typing import TypeVar, Generic

T = TypeVar('T')

class Container(Generic[T]):
    def __init__(self, item: T):
        self.item = item
        
    def get_item(self) -> T:
        return self.item



# ********************** Abstract class ********************** #
from abc import ABC, abstractmethod

class FormeAbstraite(ABC):
    @abstractmethod
    def calculer_aire(self):
        pass
        
    @abstractmethod
    def calculer_perimetre(self):
        pass
