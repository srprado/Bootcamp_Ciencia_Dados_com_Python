#(*args e **kwargs). Poderia ser quanlquer nome, o importante é o uso do asterisco
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}:{valor}" for chave, valor in kwargs.items()])
    mensagem = f"\n{data_extenso}\n{texto}\n{meta_dados}"
    print(mensagem)

exibir_poema("Quarta-feira, 10 de dezembro de 2025","Zen of Python", "Beaultiful is better than ungly...", autor="Tim Peters", ano=1999)

#a barra separa como se da a passagem de parâmetros, antes dela tudo dever ser passado de acordo com a posição
def criar_carro (modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #valido
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido