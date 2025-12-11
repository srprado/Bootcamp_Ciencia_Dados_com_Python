tupla = ("laranja", "maçã", "uva","laranja",)
print(tupla)
listas = [1,2,2,3,4,5,5,6,8]
print(listas)
print(f"""########## CONJUNTOS ##########""")
tupla_unica = set(tupla)
print(tupla_unica)

listas_unica = set(listas)
print(listas_unica)

#declarando um conjunto diretamente - não é muito utilizado
linguagens = {"python", "js", "c", "java", "python", "csharp"}
print(linguagens)

lista_linguagens = list(linguagens)
print(lista_linguagens[0])
print("\nPercorrendo elementos do conjunto:")
for item in linguagens:
    print(item)
#ou com enumerate:
for indice, item in enumerate(linguagens):
    print(f"{indice}: {item}")


