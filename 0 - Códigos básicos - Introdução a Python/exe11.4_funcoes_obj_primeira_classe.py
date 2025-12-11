#Função é um objeto de primeira classe, sendo assim é possível torná-la um parâmetro:
def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"0 resultado da operação {a} + {b} = {resultado}")

exibir_resultado (10, 10, somar) # O resultado da operação 10 + 10 = 20
exibir_resultado (10, 10, subtrair) # O resultado da operação 10 - 10 = 0

#Atribuir a função a uma variável
op = somar
print(op(1,2))