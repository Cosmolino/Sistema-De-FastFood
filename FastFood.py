print('1 - Hamburguer - R$10,00')
print('2 - Batata Frita - R$5,00')
print('3 - Refrigerante - R$4,00')
print('4 - Sorvete - R$2,00')

opcao = int(input('Digite o nº da opção desejada: '))
quantidade = int(input('Digite a quantidade desejada: '))
nome = input('Digite o nome do cliente: ')

if opcao == 1:
    print('Hamburguer sendo preparado para ', nome )
    print('Tempo de espera de 15 minutos')
    total = quantidade * 10
    print('Total: R$', total)

if opcao == 2:
    print('Batata Frita sendo preparado para ', nome )
    print('Tempo de espera de 15 minutos')
    total = quantidade * 10
    print('Total: R$', total)

if opcao == 3:
    print('Refrigerante sendo preparado para ', nome )
    print('Tempo de espera de 15 minutos')
    total = quantidade * 10
    print('Total: R$', total)

if opcao == 4:
    print('Sorvete sendo preparado para ', nome )
    print('Tempo de espera de 2 minutos')
    total = quantidade * 10
    print('Total: R$', total)