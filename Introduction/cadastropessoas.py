def cadastrar_pessoa(nome, idade, sexo, cidade):
    return f"Dados a serem cadastrados: \n Nome: {nome} \n Idade: {idade} \n Sexo: {sexo} \n Cidade: {cidade}"

mensagem = cadastrar_pessoa(str(input("Digite o nome: ")), str(input("Digite a idade ")), str(input("Digite o sexo: ")), str(input("Digite a cidade: ")))
print(mensagem)