salario = float(input("Informe seu salário: "))
nova_consulta = 1

while salario == 0:
    print("Insira um salário válido!")
    salario = float(input("Informe seu salário: "))
if salario > 0:
    if salario > 0 and salario <= 1903.98:
        print("Você está isento!")
    elif salario >= 1903.99 and salario <= 2826.65:
        ir = salario * 0.075
        print(f"Seu desconto IR é de: R$ {ir}")
        print(f"Seu salário com o desconto é de: R$ {salario - ir}")
    elif salario >= 2826.66 and salario <= 3751.05:
        ir = salario * 0.15
        print(f"Seu salário com o desconto é de: R$ {salario - ir}")
        print(f"Seu desconto IR é de: R$ {ir}")
    elif salario >= 3751.06 and salario <= 4664.68:
        ir = salario * 0.075
        print(f"Seu salário com o desconto é de: R$ {salario - ir}")
        print(f"Seu desconto IR é de: R$ {ir}")
    elif salario >= 4664.68:
        ir = salario * 0.275
        print(f"Seu salário com o desconto é de: R$ {salario - ir}")
        print(f"Seu desconto IR é de: R$ {ir}")
        


