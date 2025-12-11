#Nem todos os métodos estão expressos aqui. Olhar o arquivo "Bootcamp_Ciencia_Dados_com_Python\Anotações - Bootcamp Ciência de Dados com Python.docx"
pessoa = {"nome":"Sabrina", "idade":"25"}
#mesmo dicionário, porém usando a classe dict para declarar
pessoa2 = dict(nome="Sabrina", idade="25")
print(pessoa2["nome"])
#atribuindo valor ao dicionário
pessoa["telefone"] = 99999999999
print(pessoa)
#Dicionário aninhado
contatos={
    "pessoa1@gmail.com": {"nome":"Pessoa 1", "telefone":"11111111111"},
    "pessoa2@gmail.com": {"nome": "Pessoa 2", "telefone":"22222222222"},
    "pessoa3@gmail.com": {"nome": "Pessoa 3", "telefone":"33333333333", "extra":{"a":1}},
}
#acessando valor de dicionário aninhado
print(contatos["pessoa1@gmail.com"]["telefone"])
print(contatos["pessoa3@gmail.com"]["extra"])

#Iteração sobre um elemento:
for chave in contatos:
    print(chave, contatos[chave])
#Desse modo ele já tras a chave e o valor, no de cima é necessário passar o dicionário e a chave para que seja printado o valor da chave
for chave, valor in contatos.items():
    print(chave, valor)

#OBS: o dicionário não permite a repetição de chave, logo se eu colocar outro valor para uma chave já existente(nome igual), o valor da chave vai ser substituido
print(f"""\n########## FROMKEYS ##########""")
dicionario = dict.fromkeys(["ingredinte1", "ingrediente2", "ingrediente3"])
print(dicionario)
dicionario2 = dict.fromkeys(["nome", "idade", "telefone", "endereço"], "vazio")
print(dicionario2)

print(f"""\n########## GET ##########""")
#dicionário "contatos" declarado anteriormente
#Aqui é passado um valor padrão no segundo argumento, para que esse valor seja retornado, caso não encontre a chave
resultado = contatos.get("pessoa1@gmail.com", {})
print(resultado)

print(f"""\n########## ITEMS ##########""")
print(contatos.items())

print(f"""\n########## KEYS ##########""")
print(contatos.keys())

print(f"""\n########## POP ##########""")
print(contatos.pop("pessoa1@gmail.com", "Essa chave não existe!"))
print(contatos)

print(contatos.pop("pessoa5@gmail.com", "Essa chave não existe!"))
print(contatos)

print(f"""\n########## SETDEFAULT ##########""")
dicionario3 = {"nome": "Sabrina", "telefone":"99999999", "endereco":"rua"}
print(dicionario3)

dicionario3.setdefault("nome", "Sabrina")
print(dicionario3)

dicionario3.setdefault("idade", "25")
print(dicionario3)

print(f"""\n########## UPDATE ##########""")
print(contatos)
contatos.update({"pessoa1@gmail.com": {"nome": "Pessoa número 1"}})
print(contatos)

contatos.update({"pessoa4@gmail.com": {"nome": "Pessoa 4", "telefone":"44444444444"}})
print(contatos)

