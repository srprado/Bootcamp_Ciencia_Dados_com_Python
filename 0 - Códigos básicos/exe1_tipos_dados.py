"""FORMULÁRIO DE CADASTRO PARA ENTENDER TIPOS DE DADOS"""

"""dicionário vazio. Tipo de dado do tipo Sequência"""
dados = {} 
"""sinalizando que é uma variável do tipo int"""
res = int(input("Aceita participar? 1-Sim, 2-Não: "))

#Declarar os tipos não é necessário
if res == 1:
    #Tipo string
    nome = str(input("Nome: "))
    #Tipo inteiro
    idade = int(input("Idade: "))
    #Tipo float(ponto flutuante)
    altura = float(input("Altura: "))
    #Tipo booleano(Se digitar True, TRUE, true → vira True, senão é False)
    estudante: bool = input("É estudante? (True/False): ").lower() == "true"

    #Adicionando chave e valor ao dicionário
    dados["Nome"] = nome
    dados["Idade"] = idade
    dados["Altura"] = altura
    dados["Estudante"] = estudante


    print("Dados preenchidos:")
    for chave, valor in dados.items():
        print(f"{chave}:{valor}")

elif res == 2:
    print("Obrigada!")





