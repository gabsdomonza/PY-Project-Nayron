from math import pow

def composto(capital, juros, tempo):
    return capital * pow((1 + juros), tempo)

def simples(capital, juros, tempo):
    return (capital * juros * tempo)

continuar = 's'
while continuar == 's':

    print('Escolha qual tipo de juros você quer calcular:')
    print('1 - para Juros Simples')
    print('2 - para Juros Composto')

    while True:
        escolha = int(input('Digite a opção que você deseja (1 ou 2): '))
        if escolha in [1, 2]:
            break
        else:
            print('Opção inválida! Por favor, escolha 1 para Juros Simples ou 2 para Juros Composto.')

    capital = float(input('Qual o capital você quer aplicar? '))
    juros = float(input('Qual juros anual você terá em cima de seu capital (%)? '))
    tempo = int(input('Por quantos meses seu capital ficará rendendo? '))

    juros = juros / 100  #1% = 1 / 100
    tempo = tempo / 12

    if escolha == 1:
        valor_final_simples = simples(capital, juros, tempo)
        print(f'O montante final será de: {(valor_final_simples + capital):.02f} R$')
        print(f'Os juros de seu rendimento foram de: {valor_final_simples:.02f} R$')

    elif escolha == 2:
        valor_final_composto = composto(capital, juros, tempo)
        print(f'O montante final será de: {valor_final_composto:.02f} R$')
        print(f'Os juros de seu rendimento foram de: {(valor_final_composto - capital):.02f} R$')

    continuar = str(input('Você deseja realizar outra operação? (s/n) '))

print('\nObrigado por usar nossa calculadora!')




