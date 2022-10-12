from abc import ABC, abstractmethod
from cmath import nan
from pprint import pprint
import csv

class Cupcake(ABC):
    size = "Large"
    def __init__(self, name, cost, flavor, gluten_free, sprinkles, filling):
        self.name = name
        self.cost = cost
        self.flavor = flavor
        self.gluten_free = gluten_free
        self.sprinkles = sprinkles
        self.filling = []
    def method_add_filling_type(self, *args):
        for fillings in args:
            self.filling.append(fillings)
    @abstractmethod
    def method_calculate_price(self, quantity):
        return quantity * self.cost

class Large(Cupcake):
    size = "large"
    def method_calculate_price(self, quantity):
        return quantity * self.cost

class Medium(Cupcake):
    size = "Medium"
    def method_calculate_price(self, quantity):
        return quantity * self.cost

class Small(Cupcake):
    size = "small"
    def method_calculate_price(self, quantity):
        return quantity * self.cost 

class Mini(Cupcake):
    size = "mini"
    def __init__(self, name, cost, flavor, gluten_free, sprinkles):
        self.name = name
        self.cost = cost
        self.flavor = flavor
        self.gluten_free = gluten_free
        self.sprinkles = sprinkles
    def method_calculate_price(self, quantity):
        return quantity * self.cost 


cupcakeone = Mini("mini-chocolate explosions", 1.00, "chocolate", True, True)
cupcaketwo = Large("strawberry-bananza", 3, "strawberry", True, True, ["yes", 'yes', 'yes'])
cupcakethree = Medium("banana-split", 2, "banana", True, True, nan)
cupcakefour = Large("peach-passion", 3, 'peach', True, True, nan)
cupcakefive = Mini("mini-brownie", 1, "chocolate", True, True)
cupcakesix = Medium("banana cream", 2, 'banana',True, True, nan)
cupcakeseven = Small('cherry-filled', 1.5, 'cherry', True, True, nan)
cupcakeeight = Large('vanilla', 3, 'vanilla', True, True, nan)
cupcakenine = Mini("mini-coconut", 1, 'coconut', True, True)
cupcaketen = Large('peanut-butter', 3, 'peanut-butter', True, True, nan)


cupcake_list = [
    cupcakeone,
    cupcaketwo,
    cupcakethree,
    cupcakefour,
    cupcakefive,
    cupcakesix,
    cupcakeseven,
    cupcakeeight,
    cupcakenine,
    cupcaketen
]

current_order_list = []
print("testing 123")
def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["name", "cost", "flavor", "gluten_free", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for cupcake in cupcakes: 
            if hasattr(cupcake, "filling"):
                writer.writerow({"name": cupcake.name, "cost": cupcake.cost, "flavor": cupcake.flavor, "gluten_free": cupcake.gluten_free, "sprinkles": cupcake.sprinkles,"filling": cupcake.filling})
            else:
                writer.writerow({"name": cupcake.name, "cost": cupcake.cost, "flavor": cupcake.flavor, "gluten_free": cupcake.gluten_free, "sprinkles": cupcake.sprinkles,})


write_new_csv("displaycupcake.csv", cupcake_list)

def current_order(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["name", "cost", "flavor", "gluten_free", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for cupcake in cupcakes: 
            if hasattr(cupcake, "filling"):
                writer.writerow({"name": cupcake.name, "cost": cupcake.cost, "flavor": cupcake.flavor, "gluten_free": cupcake.gluten_free, "sprinkles": cupcake.sprinkles,"filling": cupcake.filling})
            else:
                writer.writerow({"name": cupcake.name, "cost": cupcake.cost, "flavor": cupcake.flavor, "gluten_free": cupcake.gluten_free, "sprinkles": cupcake.sprinkles,})


current_order("current_order.csv", current_order_list)

def append_list(file, cupcakes):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["name", "cost", "flavor", "gluten_free", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes: 
            if hasattr(cupcake, "filling"):
                writer.writerow({"name": cupcake.name, "cost": cupcake.cost, "flavor": cupcake.flavor, "gluten_free": cupcake.gluten_free, "sprinkles": cupcake.sprinkles,"filling": cupcake.filling})
            else:
                writer.writerow({"name": cupcake.name, "cost": cupcake.cost, "flavor": cupcake.flavor, "gluten_free": cupcake.gluten_free, "sprinkles": cupcake.sprinkles,})

append_list("displaycupcake.csv", cupcake_list)

def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)