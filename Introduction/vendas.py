valor_produto = float(input("Digite o valor do produto: "))
quantidade_produto = float(input("Digite a quantidade do produto: "))
tipo_de_pagamento = int(input("Tipos de pagamento: \n 1 - Dinheiro ou Pix \n 2 - Cartão à vista \n 3 - Cartão parcelado \n Selecione o tipo de pagamento: "))
if tipo_de_pagamento == 3:
            num_parcelas = int(input("Selecione o número de parcelas: "))
moeda = int(input("Moeda utilizada: \n 1 - Real \n 2 - Dolar \n 3 - Euro \n Seleciona a moeda utilizada: "))

def calcular_valor(valor_p, quant_p, tipo_p, moeda_p):
    v_bruto = valor_p * quant_p

    if tipo_p == 1:
        v_liquido = v_bruto - (v_bruto * (10 / 100))
    elif tipo_p == 2:
        v_liquido = v_bruto
    elif tipo_p == 3:
        v_liquido = v_bruto + ((v_bruto * (2 / 100)) * num_parcelas)
        v_parcelado = v_liquido / num_parcelas
        print(f"Serão {num_parcelas} parcelas de R$ {v_parcelado}")
    
    if moeda_p == 1:
        return v_liquido
    elif moeda_p == 2:
        return v_liquido * 5
    elif moeda_p == 3:
        return v_liquido * 5.7
    else:
        print("Moeda não cadastrada")

valor_a_pagar = calcular_valor(valor_produto, quantidade_produto, tipo_de_pagamento, moeda)

print(f"O valor final da conta é de R$ {valor_a_pagar}")
