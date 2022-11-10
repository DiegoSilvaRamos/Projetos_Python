from ast import Or
from tkinter import END


print('Bem Vindo\n')

senha = input('Insira sua senha: ')
tentativa = 0

while True | tentativa < 3:
    if not senha.isdigit():
        print('Senha invalida')
        senha = input('Insira sua senha: \n')
        tentativa = tentativa+1
        if tentativa == 2:
            print('Ecerrado !!!')
            exit()
    else:
        print('Logado\n')
        break

opcao = 1
saldo = 1000

while opcao != 0:
    opcao = int(input('[1] saldo\n[2] sacar\n[3] sair\n'))

    if opcao == 1:
        print("Seu saldo é de: ", saldo)
    elif opcao == 2:
        print('Preparando para saque...')
        break
    else:
        print("Obrigado, sistema encerrado!")
        exit()

saque = int(input('Digite o valor do saque: '))
while saque > saldo:
    saque = int(input('Saldo insuficiente, digite um novo valor: '))
    if saque <= saldo:
        print('Saque realizado com sucesso, seu saldo é: ', saque-saldo)
        print('Encerrando sessão!')
else:
    print('Saque realizado com sucesso, seu saldo é de: ', saque-saldo)
    print('Encerrando sessão')
