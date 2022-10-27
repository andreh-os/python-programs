gasolina = float(input("Insira o preço da gasolina: "))
alcool = float(input("Insira o preço do alcool: "))

def calculo_combustivel(p_gasolina, p_alcool):
    if (p_alcool / p_gasolina) <= 0.75:
        return f"Abasteça com alcool"
    elif (p_alcool / p_gasolina) > 0.75:
        return f"Abasteça com gasolina"

message = calculo_combustivel(gasolina, alcool)

print(message)