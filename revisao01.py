#EXERCICIO 2 CONDICIONAL: O CODIGO DEVE PERGUNTAR AO USUARIO SE O MESMO GOSTA MAIS DE GATOS OU DOGS;
#PERGUNTAR QUAL DAS TRÊS RAÇAS ELE GOSTA MAIS;
#SE A RAÇA CONDIZER COM A RAÇA FAVORITA DO DEV, PARABENIZAR O USUARIO, SENAO XINGAR O USUARIO.
from ast import If
quest1 = input("BEM VINDO, USUÁRIO! SE VOCÊ GOSTA MAIS DE GATOS, DIGITE 1; CASO PREFIRA CACHORROS, DIGITE 2: ") #pega o valor que o usuario digitou e armazena na variavel quest1
#quest1 tem valor 1 e 2, declara o valor que o usuario digitar
if quest1 == "1":
    quest2=input("ESCOLHA SUA RAÇA DE GATO FAVORITA: A-SIAMES, B-NORUEGUES, C-RAJADO: ")
    if quest2== "A":
        print("NOSSA, QUE BOM GOSTO!")
    else:
        print("MAU GOSTO!")
elif quest1 == "2":
    quest12=input("ESCOLHA SUA RAÇA DE CACHORRO FAVORITA: A-PASTOR ALEMAO, B-CORGI, C-BEAGLE:  ")
    if quest12=="B":
        print("NOSSA, QUE BOM GOSTO!")
    else :
        print("CORNO!")
else:
    print("VALOR INVALIDO!")