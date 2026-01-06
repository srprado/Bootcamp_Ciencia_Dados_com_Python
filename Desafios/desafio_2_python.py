# Leitura dos dados de entrada
peso = float(input("Digite o peso total da carga(toneladas): "))
preco_por_tonelada = float(input("Digite o preço por tonelada(dólar): "))
#Uma string representando o tipo de cliente ("Novo cliente", "Cliente fidelizado", "Cliente premium").
tipo_cliente = input("Qual o tipo de cliente: ")

# Calcula o valor total sem desconto
valor_total = peso * preco_por_tonelada

# TODO Aplique o desconto conforme o tipo de cliente
if(tipo_cliente.lower() == "novo cliente"):
    desconto = 0
elif(tipo_cliente.lower() == "cliente fidelizado"):
    desconto = 5
elif(tipo_cliente.lower() == "cliente premium"):
    desconto = 10
else:
    print("Cliente inválido")

valor_final = valor_total - (valor_total * desconto/100)

# Exibe o resultado formatado com duas casas decimais
print(f"{valor_final:.2f}")

