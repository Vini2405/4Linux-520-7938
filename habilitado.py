habilitado = input("Você é habilitado? ").lower().strip()
# Strip serve para rodar o programa mesmo com a existencia de algum espaço antes da resposta.

if habilitado.startswith('s'):
    print("Você pode dirigir")

elif habilitado.startswith('n'):
    print("Você nao deve dirigir...")

elif habilitado.find('s') != -1:
    print("Acho que você pode dirigir...")

else:
    print("Não entendi")
