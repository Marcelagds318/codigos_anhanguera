#pedir para o usuario digitar dois valores, perguntas qual tipo de operacao o usuario deseja realizar. Apenas + - *
from urllib import response

x = int(input("POR FAVOR, DIGITE UM VALOR: ")) #declarar valor da variavel int
y = int(input("POR FAVOR, DIGITE OUTRO VALOR: "))
a = input("QUAL TIPO DE OPERAÇÃO DESEJA REALIZAR? (1 = adicao; 2 = subtracao; 3 = multiplicação): ")
if a =="1": #laço condicional - condição
    resultado =x+y 
    print(f"O resultado da operação soma é: {resultado}")
elif a =="2":
    resultado2 = x-y
    print(f"O resultado da operação subtração é: {resultado2}")
elif a=="3":
    resultado3 = x*y 
    print(f"O resultado da operação multiplicação é: {resultado3}")
else : #else nao checa condição
    print("VALOR/OPERAÇÃO INVALIDA!")