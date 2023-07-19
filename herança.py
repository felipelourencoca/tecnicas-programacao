class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        print("O animal está fazendo um som.")

class Cachorro(Animal):
    def fazer_som(self):
        print("O cachorro está latindo.")

class Gato(Animal):
    def fazer_som(self):
        print("O gato está miando.")

# Criando objetos
animal_generico = Animal("Animal")
cachorro = Cachorro("Rex")
gato = Gato("Tom")

# Chamando o método fazer_som em cada objeto
animal_generico.fazer_som()  # Saída: O animal está fazendo um som.
cachorro.fazer_som()  # Saída: O cachorro está latindo.
gato.fazer_som()  # Saída: O gato está miando.
