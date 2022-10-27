# Quantos segundos há em 3 horas, 23 minutos e 17 segundos?
h, m, s = 3, 23, 17
s_h = (3 * 60) * 60
m_s = 23 * 60
seconds = s_h + m_s + s
print(f"{h} horas {m} minutos e {s} segundos possuem {seconds} segundos")

# Se você correr 65 quilômetros em 3 horas, 23 minutos e 17 segundos, qual é a sua velocidade média em m/s?
meters = 65 * 1000
meters_s = meters / seconds
print(f"A velocidade é de {meters_s:2f} m/s")

# Resolva essa expressão
equacao = (100 - 413 * (20 - 5 * 4)) / 5
print(equacao)

# Enivaldo quer ligar três capacitores, de valores: C1 = 10 uF | C2 = 22uF | C3 = 6.8 uF
paralelo = 10 + 22 + 6.8
serie = 1/((1/10) + (1/22) + (1/6.8))
print(f"Em paralelo: {paralelo}")
print(f"Em serie: {serie:2f}")

# Você e outros integrantes da sua república (Joca, Moacir, Demival e Jackson) foram no supermercado e compraram alguns iens:
cerveja = 2.20 * 75
macarrao = 8.73 * 2
molho = 3.45 * 1
cebola = 5.40 * 0.42
alho = 30 * 0.25
pao = 25 * 0.45
total = cerveja + macarrao + molho + cebola + alho + pao
cotinha = total / 5
print(f"A cotinha é de R$ {cotinha} para cada")

# Krissia gosta de bolinhas de queijo.  Ela quer saber quantas bolinhas de queijo dá para colocar dentro de um pote de sorvete de 2L. Ela pensou assim:
raio = 1.2
v_bolinhas = (4/3)*raio**3
v_pote = 15 * 10 * 13
quant_bolinhas = v_pote / v_bolinhas
quant_real = quant_bolinhas * 0.74
print(f"Cabem {quant_real} bolinhas")

