from math import pow  # Importa a função pow da biblioteca math para calcular potência


def composto(capital, juros, tempo):
    # Calcula o montante final usando juros compostos
    return capital * pow((1 + juros), tempo)


def simples(capital, juros, tempo):
    # Calcula o montante final usando juros simples
    return (capital * juros * tempo)


# Variável para controle do loop de repetição
continuar = 's'
while continuar == 's':

    # Exibe as opções para o usuário escolher o tipo de cálculo
    print('Escolha qual tipo de juros você quer calcular:')
    print('1 - para Juros Simples')
    print('2 - para Juros Composto')

    # Loop para garantir que o usuário digite uma opção válida
    while True:
        escolha = int(input('Digite a opção que você deseja (1 ou 2): '))
        if escolha in [1, 2]:
            break  # Sai do loop se a escolha for válida
        else:
            print('Opção inválida! Por favor, escolha 1 para Juros Simples ou 2 para Juros Composto.')

    # Solicita os valores de entrada do usuário
    capital = float(input('Qual o capital você quer aplicar? '))
    juros = float(input('Qual juros anual você terá em cima de seu capital (%)? '))
    tempo = int(input('Por quantos meses seu capital ficará rendendo? '))

    # Converte a taxa de juros anual para decimal e o tempo de meses para anos
    juros = juros / 100
    tempo = tempo / 12

    # Calcula e exibe o resultado baseado na escolha do usuário
    if escolha == 1:
        valor_final_simples = simples(capital, juros, tempo)
        print(f'O montante final será de: {(valor_final_simples + capital):.02f} R$')
        print(f'Os juros de seu rendimento foram de: {valor_final_simples:.02f} R$')

    elif escolha == 2:
        valor_final_composto = composto(capital, juros, tempo)
        print(f'O montante final será de: {valor_final_composto:.02f} R$')
        print(f'Os juros de seu rendimento foram de: {(valor_final_composto - capital):.02f} R$')

    # Pergunta ao usuário se deseja fazer outra operação
    continuar = str(input('Você deseja realizar outra operação? (s/n) '))

# Mensagem final ao sair do programa
print('\nObrigado por usar nossa calculadora!')



