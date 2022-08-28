numero = 1
while numero > 100: # enquanto numero diferente de 0
    numero = int(input("Digite um número: ")) #variavel inteira de entrada
    if numero % 2 == 0: #se numero dividido por 2 é igual a 0, numero par
        print("Número par!")
    else:
        print("Número ímpar!") # senao, numero impar