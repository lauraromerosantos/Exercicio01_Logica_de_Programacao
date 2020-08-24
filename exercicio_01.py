''' Trabalho Individual
    Aluna: Laura Romero
'''
opcoes = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
sistemas = [0] * 6
print('Escolha uma opção: \n 1- Windows Server \n 2- Unix \n 3- Linux \n 4- Netware \n 5- Mac OS \n 6- Outro \n')
while True:
    while True:
        opcao = int(input('Digite a opção escolhida: '))
        if opcao > 6 or opcao < 0:
            print('Opção inválida')
        else:
            break
    if opcao == 0:
        break
    sistemas[opcao - 1] = sistemas[opcao - 1] + 1

print('Sistema Operacional    Votos  %')
print('----------------------------------')
cont = 0
perc = 0
melhor = 0
melhorSistema = ''
for s in sistemas:
    print('%s    %d    %.1f%%' % (opcoes[cont], s,(s * 100) / sum(sistemas) ))
    if s > melhor:
        melhor = s
        melhorSistema = opcoes[cont]
        perc = (s * 100) / sum(sistemas)
    cont += 1

print('----------------------------------')
print('Total   %d' % sum(sistemas))
print('O Sistema Operacional mais votado foi o %s, com %d votos, correspondendo a %.2f dos votos.' % (melhorSistema, melhor, perc))
