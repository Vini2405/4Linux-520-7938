ano_nascimento = int(input("Informe o ano do seu nascimento: "))

if ano_nascimento <= 1964:
    print("Você é da geração Baby Boomer!")

elif ano_nascimento <= 1979:
    print("Você é da geração X!")

elif ano_nascimento <= 1994:
    print("Você é da geração Y!")

else:
    print("Você é da geração Z!")
