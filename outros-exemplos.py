from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Retangulo(Forma):
    def area(self):
        # Implementação do cálculo da área para retângulo
        pass

    def perimetro(self):
        # Implementação do cálculo do perímetro para retângulo
        pass

class Circulo(Forma):
    def area(self):
        # Implementação do cálculo da área para círculo
        pass

    def perimetro(self):
        # Implementação do cálculo do perímetro para círculo
        pass

def calcular_area(objeto):
    return objeto.area()

retangulo = Retangulo()
circulo = Circulo()

print(calcular_area(retangulo))  # Chama o método area() de Retangulo
print(calcular_area(circulo))  # Chama o método area() de Circulo
