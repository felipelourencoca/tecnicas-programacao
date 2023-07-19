from abc import ABC, abstractmethod

class Animal:
    @abstractmethod
    def fazer_som(self)
        pass


class Cachorro(Animal):
    def fazer_som(self):
        print("Auauauaua")

class Gato(Animal):
    def fazer_som(self):
        print("Miauuu")


g = Gato()
g.fazer_som()

g = Cachorro()
g.fazer_som()

g = Animal()
g.fazer_som()