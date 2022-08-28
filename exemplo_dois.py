texto = """aeiou

fdy
12345
""" #para que um texto apareca na tela do usuario, se utiliza aspas triplas 
#ja que aspas duplas e simples sao para strings pequenas
vogal = 0
consoante = 0
for caracter in texto: #mostra a posição no texto a letra 
    if caracter in 'aeiou':
        vogal+=1 #o compilador busca as vogais minusculas no texto
    elif caracter in 'bcdfghjklmnpqrstvwxyz':
        consoante+=1
    else :
        continue
    #aspas triplas quebram linha de texto, tambem cria comentarios de varias linhas 
print("O numero de vogais é igual a: "+ str(vogal)+"\nE o numero de consoantes é igual a: " +str(consoante)) 
#mostrar na tela do usuario, as vogais a e e minusculas da palabGra que ele digitou
