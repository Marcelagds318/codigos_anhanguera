from operator import truediv

#elif faz o else continuar tendo sentido
pers= input("Digite o nome de um personagem à sua escolha: ")
test= int(input(" de 0 a 100, digite o nível de força do personagem em questão: "))
stars = 3
if test <25:
    stars-=1
if test<=10 :
    stars-=1
if test<=0:
    stars-=1
if test>=75:
    stars+=1
if test >=90:
    stars+=1
if test >=100:
    stars+=1
print(f"SEU PERSONAGEM POSSUI: {stars}  estrelas!")
if stars==0:
    print(f"Pensei que haviam limites para fraqueza, mas {pers} é incomparável nesta arte. Um dos mais fracos de toda a história!") 
if stars==1:
    print(f"Mas que absurdo! {pers} é mais fraco do que uma criança!")
if stars ==2:
    print(f"Que fracote! {pers}")
if stars==3:
    print(f"Meh... {pers} é mediano.")
if stars ==4:
    print(f"Le {pers} é bem roubado até!" )
if stars==5:
    print(f"Mas que absurdo! {pers} é de nível mundial!")
if stars ==6:
    print(f"Incrível... {pers} é tão poderoso quanto um deus!")