class Pessoa:
    def __init__(self,nome):
        self._nome = nome

    def mostrar_documento(self):
        pass

class Fisica(Pessoa):
    def __init__(self,nome,cpf):
        super().__init__(nome)
        self._cpf = cpf

    def mostrar_documento(self):
        print(self._cpf)

class Juridica(Pessoa):
    def __init__(self,nome,cnpj):
        super().__init__(nome)
        self._cnpj = cnpj

    def mostrar_documento(self):
        print(self._cnpj)



f1 = Fisica("Fulano","232323232")
j1 = Juridica("Beltrano", "5656565665")


f1.mostrar_documento()
j1.mostrar_documento()


def mostrar_doc(pe):
    return pe.mostrar_documento()

print("=====")
mostrar_doc(f1)
mostrar_doc(j1)




#print(len("Fulano"))
#print(len([10,20,30]))


'''
def somar(v1,v2, v3 = 0):
    print(v1 + v2 + v3)


somar(2,2)
somar(2,3,4)

'''