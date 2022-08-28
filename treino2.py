x = int(input("digite um valor inteiro: "))
if x >= 0 :
    print("bolo")
elif x< 0 : #apenas quando vamos utilizar o else, continua a condição do if
    print("camelo")
else: #obedece o elif
    print("VALOR INVALIDO!")
#o compilador le de cima para baixo
#o else obedece o elif e o elif obedece o if