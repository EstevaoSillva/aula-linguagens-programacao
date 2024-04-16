from datetime import datetime

busca = input('Digite um nome: \n')
busca_nome, busca_sobrenome = busca.split()
busca_nome = busca_nome.lower()
busca_sobrenome = busca_sobrenome.lower()

with open('alunos.csv', 'r') as arquivo:
    next(arquivo)
    lista_linhas = arquivo.readlines()
    for linha in lista_linhas:
        nome_completo, data_nascimento, matricula = linha.strip('\n').split(',')

        #separar nome dos numeros
        nome, sobrenome, numero= nome_completo.split(" ")
        nome = nome.lower()
        sobrenome = sobrenome.lower()
        # fim separa nome dos numeros
        
        if (nome == busca_nome and sobrenome == busca_sobrenome):
            data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
            data_atual = datetime.now()
            idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day)) 
            print(nome_completo, '>', idade)