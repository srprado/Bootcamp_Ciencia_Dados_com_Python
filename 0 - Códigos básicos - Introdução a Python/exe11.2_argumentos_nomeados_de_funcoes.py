#Argumentos nomeados
def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}, {modelo}, {ano}, {placa}")
##passar nomeado, garante que cada parâmetro vai receber o valor certo, independente da ordem que for passado
salvar_carro(marca="Fiat", modelo="Palio", ano="2000", placa="ZZZZ-111")
salvar_carro(marca="Volkswagen", placa="XXXX-111", modelo="Gol", ano="2010")
#A desvantagem desse método de passagem de parâmetros é que se alterar o nome do argumento na função e não usar 
#o correto na hora de chamar vai dar erro

#Convertendo a passagem de parâmetros para um dicionário(**)
salvar_carro(**{"marca": "Fiat", "modelo": "Uno", "ano": 1999, "placa":"YYYY-3333"})

