adicao = lambda x, y: x + y
subtracao = lambda x, y: x - y
multiplicacao = lambda x, y: x * y
divisao = lambda x, y: x / y

while True:
    x = float(input('Digite o valor de x: '))
    operacao = input('Digite a operação desejada: ').lower()
    y = float(input('Digite o valor de y: '))

    if operacao == '+':
        print()
        resultado = adicao(x, y)
        print(f'O valor da soma é: {resultado}')
        break

    elif operacao == '-':
        print()
        resultado = subtracao(x, y)
        print(f'O valor da subtração é: {resultado}')
        break

    elif operacao == '*':
        print()
        resultado = multiplicacao(x, y)
        print(f'O valor da multiplicação é: {resultado}')
        break

    elif operacao == '/':
        print()
        resultado = divisao(x, y)
        print(f'O valor da divisão é: {resultado}')
        break

    else:
        print()
        print('Operação inválida! Digite uma das opções a seguir: +, -, * ou /.')
