lista = []

while True:
    dados = []

    nome = str(input('Digite o nome: ')).strip()
    n1 = float(input('Digite a nota 1: '))
    n2 = float(input('Digite a nota 2: '))

    media = n1+n2/2

    dados.append(nome)
    dados.append(n1)
    dados.append(n2)
    dados.append(media)

    continuar = str(input('Deseja continuar ? [S/N]: ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Opção inválida ! Digite [S] para SIM e [N] para não. Deseja continuar ? [S/N]: '))

    if continuar == 'N':
        lista.append(dados[:])
        break
    else:
        lista.append(dados[:])

print('='*55)
print('LISTAGEM DE PREÇOS'.center(55))
print('='*55)

for pos in range(0,len(lista)):
