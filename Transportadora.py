# função dimensoesObjeto criada para solicitar ao usuário a altura, comprimento e largura do objeto.
# função com a equação para saber o volume do objeto.
def  dimensoesObjeto():
    # criado um loop com as devidas condições para sair dele e continuar o código.
    while True:
        # criado um loop dentro do loop para válidar.
        while True:
            # válida se os dados recebidos são númericos.
            try:
                alt = float(input('Digite a altura do objeto (em cm): '))
                comp = float(input('Digite o comprimento do objeto (em cm): '))
                larg = float(input('Digite a largura do objeto (em cm): '))
                # para essa etapa se os dados recebidos passarem na validação.
                break
            # caso de erro de tipo ou valor, mostra que foi digitado algo não númerico e volta para pedir os dados.
            except(ValueError, TypeError):
                print('Foi digitado algo não númerico.\n'
                      'Favor tentar novamente.\n')
        # equação para calcular o volume.
        vol = alt * comp * larg
        # mostra na tela o resultado da equação.
        print('O volume é {}cm³'.format(vol))

        # caso o valor dê 100000m³, avisa ao usuário que é uma dimensão muito grande e pede para tentar outros valores.
        if vol >= 100000:
            print('Não trabalhamos com objetos de tamanha dimensão.\n'
                  'Tente com outros valores.\n')
        # caso o valor seja menor que 100000m³ ou maior/igual a 30000, retorna o valor de 50.
        elif 30000 <= vol < 100000:
            return 50
        # caso o valor seja menor que 30000m³ ou maior/igual a 10000, retorna o valor de 30.
        elif 10000 <= vol < 30000:
            return 30
        # caso o valor seja menor que 10000m³ ou maior/igual a 1000, retorna o valor de 20.
        elif 1000 <= vol < 10000:
            return 20
        # caso o valor seja menor que 1000m³, retorna o valor de 10.
        elif vol < 1000:
            return 10


# função pesoObjeto criada para solicitar ao usuário o peso do objeto.
def pesoObjeto():

    # criado um loop com as devidas condições para sair dele e continuar o código.
    while True:
        # criado um loop dentro de um loop para válidar.
        while True:
            # válida se os dados recebidos são númericos.
            try:
                peso = float(input('Qual o peso do objeto? (em kg): '))
                # para essa etapa se os dados recebidos passarem na validação.
                break
            # caso de erro de tipo ou valor, mostra que foi digitado algo não númerico e volta para pedir o peso.
            except(ValueError, TypeError):
                print('Valor inválido!\n'
                      'Digite o peso novamente.\n')
        # caso o peso seja maior que 30kg, avisa que é muito pesado e pede para tentar novamente.
        if peso > 30:
            print('Não trabalhamos com objetos tão pesados!\n'
                  'Tente um objeto com outro peso.\n')
        # caso o peso seja maior que 10kg ou menor/igual a 30kg, retorna 3.
        elif 10 < peso <= 30:
            return 3
        # caso o peso seja maior que 1kg ou menor/igual a 10kg, retorna 2.
        elif 1 < peso <= 10:
            return 2
        # caso o peso seja maior que 0.1kg ou menor/igual a 1kg, retorna 1.5.
        elif 0.1 < peso <= 1:
            return 1.5
        # caso o peso seja menor/igual a 0.1, retorna 1.
        elif peso <= 0.1:
            return 1


# função rotaObjeto criada para solicitar ao usuário a rota desejada.
def rotaObjeto():

    # criado um loop com as devidas condições para sair dele e continuar o código.
    while True:
        # mostra para o usuário as opções de rotas.
        print(' CWB/BRZ - De Curitiba para Borrazópolis\n'
              ' BRZ/CWB - De Borrazópolis para Curitiba\n'
              ' NLR/BRZ - De Nova Laranjeiras para Borrazópolis\n'
              ' BRZ/NLR - De Borrazópolis para Nova Laranjeiras\n'
              ' NLR/CWB - De Nova Laranjeiras para Curitiba\n'
              ' CWB/NLR - De Curitiba para Nova Laranjeiras\n')
        # solicita ao usuário a sigla da rota que deseja.
        rota = input('Digite a sigla da rota desejada: ')
        # se a rota escolhida foi CWB/BRZ, retorna o valor 1.
        if rota == 'CWB/BRZ':
            return 1
        # se a rota escolhida foi BRZ/CWB, retorna o valor 1.
        elif rota == 'BRZ/CWB':
            return 1
        # se a rota escolhida foi NLR/BRZ, retorna o valor 1.2.
        elif rota == 'NLR/BRZ':
            return 1.2
        # se a rota escolhida foi BRZ/NLR, retorna o valor 1.2.
        elif rota == 'BRZ/NLR':
            return 1.2
        # se a rota escolhida foi NLR/CWB, retorna o valor 1.5.
        elif rota == 'NLR/CWB':
            return 1.5
        # se a rota escolhida foi CWB/NLR, retorna o valor 1.5.
        elif rota == 'CWB/NLR':
            return 1.5
        # caso o usuário digitar algo que não seja nenhuma das siglas, avisa que está errado e pergunta novamente.
        else:
            print('Rota inválida!\n'
                  'Favor digitar a rota desejada corretamente.')
            continue


# mostra na tela um bem vindo e minha identificação.
print('Bem vindo a Transportes Lucas Gabriel de Moura Santos LTDA (RU: 3927427)')
# criado uma variável onde é atribuido a função dimensoesObjeto.
d = dimensoesObjeto()
# criado uma variável onde é atribuido a função pesoObjeto.
p = pesoObjeto()
# criado uma variável onde é atribuido a função rotaObjeto.
r = rotaObjeto()
# variável onde é atribuido a equação final para o valor do transporte.
vf = d * p * r
# mostra na tela o total a pagar com as opções selecionadas.
print('Valor total a pagar é: R${:.2f}'.format(vf))
