print(f"""########## DECLARANDO LISTAS ##########""")
frutas = ["laranja", "maçã", "uva"]
print(frutas)

frutas2 = []
print(frutas2)

letras = list("python")
print(letras)

numeros = list(range(10))#range vai criar numero de 0 a 9
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

print(f"""\n########## ACESSO DIRETO ##########""")
frutas = ["maçã", "laranja", "uva", "pera"]
print(frutas[0])  # maçã
print(frutas[2])  # uva

print(f"""\n########## ÍNDICES NEGATIVOS ##########""")
frutas = ["maçã", "laranja", "uva", "pera"]
print(frutas[-1])  # pera
print(frutas[-3])  # laranja

print(f"""\n########## MATRIZ ##########""")
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

print(f"""\n########## FATIAMENTO ##########""")
lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]

print(f"""\n########## ITERAR LISTAS ##########""")
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

print(f"""\n########## COMPREENSÃO DE LISTAS ##########""")
# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)

print(f"""\n########## APPEND ##########""")
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)  # [1, "Python", [40, 30, 20]]

print(f"""\n########## CLEAR ##########""")
lista = [1, "Python", [40, 30, 20]]
print(lista)  # [1, "Python", [40, 30, 20]]
lista.clear()
print(lista)  # []

print(f"""\n########## COPY ##########""")
lista = [1, "Python", [40, 30, 20]]
lista.copy()
print(lista)  # [1, "Python", [40, 30, 20]]

print(f"""\n########## COUNT ##########""")
cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1

print(f"""\n########## EXTEND ##########""")
linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]

print(f"""\n########## INDEX ##########""")
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

print(f"""\n########## POP ##########""")
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp
print(linguagens.pop())  # java
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python

print(f"""\n########## REMOVE ##########""")
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.remove("c")
print(linguagens)  # ["python", "js", "java", "csharp"]

print(f"""\n########## REVERSE ##########""")
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.reverse()
print(linguagens)  # ["csharp", "java", "c", "js", "python"]

print(f"""\n########## SORT ##########""")
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)

print(f"""\n########## LEN ##########""")
linguagens = ["python", "js", "c", "java", "csharp"]
print(len(linguagens))  # 5

print(f"""\n########## SORTED ##########""")
linguagens = ["python", "js", "c", "java", "csharp"]
print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]
