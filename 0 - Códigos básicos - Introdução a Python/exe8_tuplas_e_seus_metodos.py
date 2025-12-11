print(f"""########## DECLARANDO TUPLAS ##########""")
frutas = ("laranja", "maçã", "uva",)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1,2,3,4])
print(numeros)

pais = ("Brasil",)

print(f"""\n########## ACESSO DIRETO ##########""")
frutas = ("laranja", "maçã", "uva",)
print(frutas[0])  # laranja
print(frutas[2])  # uva

print(f"""\n########## ÍNDICES NEGATIVOS ##########""")
frutas = ("laranja", "maçã", "uva",)
print(frutas[-1])  # uva
print(frutas[-2])  # laranja

print(f"""\n########## MATRIZ ##########""")
matriz = [
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
]

print(matriz[0])  # (1, "a", 2)
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

print(f"""\n########## FATIAMENTO ##########""")
tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:])  # ("t", "h", "o", "n")
print(tupla[:2])  # ("p", "y")
print(tupla[1:3])  # ("y", "t")
print(tupla[0:3:2])  # ("p", "t")
print(tupla[::])  # ("p", "y", "t", "h", "o", "n")
print(tupla[::-1])  # ("n", "o", "h", "t", "y", "p")

print(f"""\n########## ITERAR LISTAS ##########""")
carros = ("gol", "celta", "palio",)

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

print(f"""\n########## COUNT ##########""")
cores = ("vermelho", "azul", "verde", "azul",)

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1

print(f"""\n########## INDEX ##########""")
linguagens = ("python", "js", "c", "java", "csharp",)

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

print(f"""\n########## LEN ##########""")
linguagens = ("python", "js", "c", "java", "csharp",)
print(len(linguagens))  # 5
