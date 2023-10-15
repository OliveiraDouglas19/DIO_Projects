menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input('Digite o valor do depósito: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito de {valor: .2f}\n'
        else:
            print('Operação falhou, valor inválido')


    elif opcao == "s":
        valor = float(input('Digite o valor do saque: '))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou, saldo insuficiente')

        elif excedeu_limite:
            print('Operação falhou, limite de saque excedido')

        elif excedeu_saques:
            print('Operação falhou, limite de saques excedido')
        
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque de {valor: .2f}\n'
            numero_saques += 1

    
    elif opcao == "e":
        print("\n======================== EXTRATO ========================")
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo: .2f}')
        print("===========================================================")

    elif opcao == "q":
        print('Saindo...')
        break

    else:
        print('Operação inválida, favor selecione novamente a opção desejada')
    