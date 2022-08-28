nome = input("digite o seu nome: ") #abre caixa de texto para digitarmos o valor
x = input("digite a sua idade:   ") #inputar dados
situacao_inscricao = True
teste = True
while teste==True:
    nota= float(input("Digite sua nota: "))
    if nota <0 or nota>100: #and esta errado, nota n é maior e menor ao mesm tempo
        print(input("por favor, digite uma nota válida!"))
    else :
        print(f" {nome} QUE TIROU  {nota} e tem {x} anos está inscrito: {situacao_inscricao}")
        print(type(x))
        print(type(nome))
        print(type(nota))
        print(type(situacao_inscricao))
        if nota <51:
            print("NOTA ABAIXO DA MÉDIA!")
    resp=(input('DESEJA CONTINUAR REALIZANDO A OPERAÇÃO? (s/n) '))
    if resp=="s":
        continue
    if resp =="n":
        teste = False
    else:
        print("POR FAVOR, DIGITE UMA RESPOSTA VÁLIDA!")

