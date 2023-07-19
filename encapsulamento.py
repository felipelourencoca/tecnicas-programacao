class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self.__idade = idade
    
    def saudacao(self):
        print(f"Olá, meu nome é {self._nome} e eu tenho {self.__idade} anos.")

    def __metodo_privado(self):
        print("Este é um método privado.")

# Criando uma instância da classe Pessoa
p1 = Pessoa("João", 25)

# Acesso aos atributos
print(p1._nome)  # Saída: João
print(p1._Pessoa__idade)  # Saída: 25

# Chamada de métodos
p1.saudacao()  # Saída: Olá, meu nome é João e eu tenho 25 anos.
p1._Pessoa__metodo_privado()  # Saída: Este é um método privado.
