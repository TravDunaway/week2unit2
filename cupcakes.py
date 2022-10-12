from cmath import nan
from abc import ABC, abstractmethod
from pprint import pprint
import csv


# with open("cupcake.csv") as csvfile:
#     pass


class Cupcake(ABC):
    size = "Large"
    def __init__(self, name, cost, flavor, gluten_free, sprinkles, filling):
        self.name = name
        self.cost = cost
        self.flavor = flavor
        self.gluten_free = gluten_free
        self.sprinkles = sprinkles
        self.filling = []
    def method_one(self):
        pass
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

cupcakeone = Large("chocolate-plain", 2.00, "chocolate", True, True, nan)
cupcakeone.method_add_filling_type("strawberry-jelly", "lemon-custard", "peanut-butter-blast")

class Medium(Cupcake):
    size = "Medium"
    def method_calculate_price(self, quantity):
        return quantity * self.cost

cupcaketwo = Medium("strawberry-goodness", 1.50, "strawberry, dum dum", True, True, nan)
cupcaketwo.method_add_filling_type("strawberry Jelly")

class Small(Cupcake):
    size = "small"
    def method_calculate_price(self, quantity):
        return quantity * self.cost 

cupcakethree = Small("vanilla-swirl", 1, "vanilla", True, False, nan)
cupcakethree.method_add_filling_type("swirly stuff")

# This is how you would change the values of the attributes--
cupcakeone.cost = 1.5
cupcakeone.name = "chocolate-plain-on-sale"
cupcakeone.sprinkles = False
# You could add attributes that didn't exist before--
# cupcakeone.shapes = "square"
# print(cupcakeone.filling)

# This is how to create a child class:
# class Mini(Cupcake):
#     size = "mini"
# This is, for example, if you wanted to not have the option of filling, for the mini cupcakes.
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
      






cupcaketwomini = Mini("chocolate-blast", 1.00, "chocolate", True, True)
# print(cupcaketwomini.cost)
# print(cupcaketwomini.flavor)
# print(cupcaketwomini.gluten_free)
# print(cupcaketwomini.size)

cupcake_list = [
    cupcakeone,
    cupcaketwo,
    cupcakethree,
    cupcaketwomini
]
def print_cupcake_list():
    for cupcake in cupcake_list:
        print(cupcake)

# print_cupcake_list()


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


write_new_csv("sample.csv", cupcake_list)

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

append_list("sample.csv", cupcake_list)

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

# def add_cupcake_dictionary(file, cupcake):
#     with open(file, "a", newline="\n") as csvfile:
#         fieldnames = ["size", "name", "cost", "flavor", "gluten-free", "sprinkles", "filling"]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writerow(cupcake)
    

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        for row in reader:
            pprint(row)

read_csv("sample.csv")