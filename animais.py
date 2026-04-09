perguntas = [['Seu animal gosta de bananas', 'macaco'], ]


while True:
    print ('pense em um animal')

    acertou = False
    for pergunta in perguntas:
        resposta = input(f'{pergunta[0]}(s/n): ')
        if resposta.lower() == 's':
            print( f'Voce pensou em um {pergunta[1]}')
            acertou = True
            break
    
    if not acertou :
        animal = input('Desisto! Em qual animal voce pensou?')
        nova_pergunta = input('Qual pergunta voce faria para diferenciar esse animal?')
        perguntas.append([ nova_pergunta, animal])
        
    resposta = input('Quer jogar novamente? (s/n): ')
    if resposta.lower() != 's':
       print ('Ok, foi bom jogar com voce')
       break
       