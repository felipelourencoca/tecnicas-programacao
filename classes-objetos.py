


print("Ola")



class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        print(f"Ola. Meu nome é: {self.nome} e tenho {self.idade}")
        print("Ola. Meu nome é: " + self.nome)

class Fisica(Pessoa):
    def __init__(self,nome,idade):
        super().__init__(nome,idade)
    
    def saudacaoFisica(self):
        print("Eu sou uma pessoa Fisica")

p1 = Pessoa("Felipe",37)
p1.saudacao();

p2 = Fisica("Fulano",40)

p2.saudacaoFisica() 

