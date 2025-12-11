def calcular_total(numeros):
    return sum(numeros)

def retorna_antecesso_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(calcular_total([10,20,30]))
print(retorna_antecesso_e_sucessor(8))

#Por padrão as funções retornam 'None'
def funcao_none():
    print("Hello")
print(funcao_none())