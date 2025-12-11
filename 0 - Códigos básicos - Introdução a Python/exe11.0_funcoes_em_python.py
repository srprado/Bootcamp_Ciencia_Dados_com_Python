def exibir_hello_word():
    print("Hello Word!!")

#Aqui é necessário passar um valor para o parâmetro
def exibir_nome(nome):
    print(f"exibir_nome() -> Seu nome é {nome}")

#Aqui eu declarei um valor default para o parâmetro, se não passar nada ele imprime 'Sabrina', 
#se passar algo, vai imprimir o valor que foi passado.
#se o parâmetro tiver valor fixo, pode ser passado sem a variável também -> ("Sabrina")
def exibir_nome2(nome="Sabrina"):
    print(f"exibir_nome2() -> Seu nome é {nome}")

exibir_hello_word()
exibir_nome("Maria")
exibir_nome2()
exibir_nome2("José")