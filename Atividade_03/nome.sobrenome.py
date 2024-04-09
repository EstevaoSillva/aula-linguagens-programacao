nome = (input("Digite seu nome: "))
sobrenome = (input("Digite seu sobrenome: "))

print(sobrenome, ',', nome[0], sep='') 

len(nome)
tamanho = len(nome)

ultima_letra = nome[tamanho -1]
print(f"A última letra do seu nome é {ultima_letra}.")