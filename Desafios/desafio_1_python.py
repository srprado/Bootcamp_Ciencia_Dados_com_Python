def calculo_salario(salario_bruto, beneficios):
    percent = 0
    if(salario_bruto <= 11000):
        percent = 5
    elif(salario_bruto > 1100 and salario_bruto <=2500):
        percent = 10
    else:
        percent = 15
    
    return salario_bruto - ((salario_bruto*percent)/100) + beneficios



salario_bruto = float(input("Digite seu salário bruto: "))
beneficios = float(input("Digite o valor dos benfícios: "))

salario_liquido = calculo_salario(salario_bruto, beneficios)
print(f"O valor do salário a receber é de R${salario_liquido:.2f}")