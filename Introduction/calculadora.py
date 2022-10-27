firstnumber = int(input("Digite o primeiro número: "))
secondnumber = int(input("Digite o segundo número: "))
operator = int(input("Operações \n 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n Selecione o operador: "))

if operator == 1 :
    print(f"O resultado é: {firstnumber + secondnumber}")
elif operator == 2 :
    print(f"O resultado é: {firstnumber - secondnumber}")
elif operator == 3 :
    print(f"O resultado é: {firstnumber * secondnumber}")
elif operator == 4 :
    print(f"O resultado é: {firstnumber / secondnumber}")