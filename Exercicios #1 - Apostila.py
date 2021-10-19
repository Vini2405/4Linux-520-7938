# Exercicio 1
nome = input("Informe o seu nome: ")
cpf = input("Informe o seu CPF: ")
idade = input("Informe a sua idade: ")

print('-----------------------')
print('Confirmação de cadastro:')
print(f'Nome: {nome}')
print(f'CPF: {cpf}')
print(f'Idade: {idade}')
print('-----------------------')

# Exercicio 2
frase = "Umxpratoxdextrigoxparaxtrêsxtigresxtristes"
frase = frase.replace('x', ' ')
print(f'{frase}')

# Exercicio 3

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
soma = num1 + num2
diferenca = num1 - num2
print(f'A soma dos dois número é: {soma}')
print(f'A diferença dos dois número é: {diferenca}')
