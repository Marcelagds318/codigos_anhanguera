a =2 #declaro variavel de equação
b=0 #variavel de equacao

equa = input("DIGITE A FORMULA GERAL DA EQUACAO LINEAR (a*x+b):     ") #assumo um valor de entrada
print(f"\nA entrada do usuario {equa} é do tipo {type(equa)} ") #a nova variavel imprime a equacao e o tipo

for x in range(10): #para x em range cria 10 numeros em sequencia
    y= eval(equa) #nova variavel declarada com a função de build in que avalia a equacao digitada pelo usuario como expressao
    print(f"\nResultado da equação para x = {x} é {y}") #imprime o resultado da equacao com a declaracao de variaveis x e y e f para numeros
