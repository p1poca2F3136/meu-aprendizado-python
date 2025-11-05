nome = input("Digite seu nome:")

nome = str(nome)

teste = type(nome)

print(teste)



try:
    # 2. Exceções e Conversão de Tipo
    idade_texto = input("Quantos anos você tem? ")
    idade = int(idade_texto)

    # 3. Condicionais (if/else)
    if idade >= 18:
        print(f"Olá, {nome}! Você é maior de idade.")
    else:
        print(f"Olá, {nome}! Você é menor de idade.")

except ValueError:
    print("Erro: Você não digitou um número válido para a idade.")


print("Fim do programa.")
