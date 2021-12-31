# Uma classe que controla o cadastro de pessoas
from time import sleep


class Cadastrar:
    def __init__(self, nome_arq):
        self.nome_arquivo = nome_arq

    def cadastrar(self, nome, idade, peso):
        with open(self.nome_arquivo, 'a') as arq:
            arq.write(f'{nome}${idade}${peso}\n')

    def apagar(self, nome):
        with open(self.nome_arquivo, 'r') as arq:
            linhas = arq.readlines()
        
        achou = False
        for n, linha in enumerate(linhas):
            linha = linha.split('$')
            if linha[0] == nome:
                linhas.remove(linhas[n])
                achou = True
        
        if achou:
            with open(self.nome_arquivo, 'w') as arq:
                for linha in linhas:
                    arq.write(linha)
    
    def mostrar(self, nome=''):
        with open(self.nome_arquivo, 'r') as arq:
            linhas = arq.readlines()

        for linha in linhas:
            linha = linha.replace('\n', '')
            linha = linha.split('$')
            if nome != '' and nome != linha[0]:
                continue
            print(f'Nome: {linha[0]}, Idade: {linha[1]}, Peso: {linha[2]}')




Arq = Cadastrar('arqivo.txt')

def menu(arg1, arg2, arg3):
    print("=" * 50)
    print(arg1)
    print(arg2)
    print(arg3)
    print("=" * 50)

def opcao1():
    while True:
        print('=-' * 25)
        print('Opcão 1')
        nome = str(input('Qual o nome da pessoa: '))
        idade = str(input('Qual a idade da pessoa: '))
        peso = str(input('Qual o peso da pessoa: '))

        print(f'nome: {nome}, idade: {idade}, peso: {peso}')
        confere = str(input('Confere [s/n]: ')).lower().strip()[0]

        if confere == 's':
            print('Salvando...')
            sleep(1)
            print('Salvo.')
            print('=-' * 25)
            break
        else:
            print('=-' * 25)
        
    Arq.cadastrar(nome, idade, peso)

def opcao2():
    while True:
        print('=-' * 25)
        print('Opção 2')
        nome = str(input('Qual o nome para apagar: ')).strip()
        print(f'nome: {nome}')

        confere = str(input('Confere [s/n]: ')).strip().lower()[0]
        if confere == 's':
            print('Apagando...')
            sleep(1)
            print('Apagado')
            print('=-' * 25)
            break
        
    Arq.apagar(nome)

def opcao3():
    while True:
        print('Opção 3')
        nome = ''
        tudo = str(input('Quer ver tudo? [s/n]: ')).strip().lower()[0]
        if tudo in 'n':
            nome = str(input('Qual o nome da pessoa: ')).strip()
        
        Arq.mostrar(nome)

        sair = str(input('Deseja sair? [s/n]: ')).lower().strip()[0]
        if sair in 's':
            print('Saindo...')
            sleep(1)
            print('=-' * 25)
            break



while True:
    print('Bem vindo ao cadastro de pessoas!')
    sleep(0.3)
    
    menu('1 - Cadastrar', '2 - Apagar', '3 - Pesquisar')

    while True:
        opcao = str(input('Sua escolha: ')).strip()[0]
        sleep(0.5)
        if opcao not in '123':
            print('Escolha uma opção válida.')
            print('-' * 50)
        else:
            break
    
    if opcao == '1':
        opcao1()
    
    elif opcao == '2':
        opcao2()
    
    elif opcao == '3':
        opcao3()
            