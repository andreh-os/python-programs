# Operadores Condicionais

# a < b
# a <= b 
# a > b
# a >= b
# a == b
# a != b
# a is b
# a is not b

# IF, ELIF, ELSE

# a = 5
# b = 10

# if a < b:
#     print("a é menor do que b")
#     r = a + b
#     print(r)
# elif a == b:
#     print("a é igual a b")
# else:
#     print("a é maior do que b")
#     r = a - b
#     print(r)

# qtde_faltas = int(input("Digite a quantidade de faltas: "))
# media_final = float(input("Digite a média final: "))

# if qtde_faltas <= 5 and media_final >= 7:
#     print("Aluno aprovado!")
# else:
#     print("Aluno reprovado!")

# # WHILE, FOR

# numero = 1
# while numero != 0:
#     numero = int(input("Digite um número: "))
#     if numero % 2 == 0:
#         print("Número par!")
#     else:
#         print("Número ímpar!")

# nome = "Guido"
# for i, c in enumerate(nome):
#     print(f"Posição = {i}, valor = {c}")

# # RANGE, BREAK, CONTINUE

# for x in range(5):
#     print(x)

# disciplina = "Linguagem de Programação"
# for c in disciplina:
#     if c=='a':
#         break
#     else:
#         print(c)
#         disciplina = "Linguagem de Programação"
        
# for c in disciplina:
#     if c=='a':
#         continue
#     else:
#         print(c)

import enum


texto = 'A inserção de comentários no código do programa é uma prática normal. Em função disso, toda linguagem de programação tem alguma maneira \
        de permitir que comentários sejam inseridos nos programas. O objetivo é adicionar descrições em partes do código, seja para documentá-lo \
        ou para adicionar uma descrição do algoritmo implementado (BANIN, 2018, p. 45).'

for i, c in enumerate(texto):
    if c == 'a' or c == 'e':
        print(f"Volga '{c}' encontrada, na posição {i}")
    else:
        continue