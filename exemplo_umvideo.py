from time import pthread_getcpuclockid


nome = input("DIGITE SEU NOME: ")
print("Olá %s, bem-vindo à disciplina de formatação. Parabéns pelo seu primeiro hello world"% (nome))
#na linguagem c ele busca a variavel e imprime na nossa tela.

nome = input("DIGITE UM NOME: ")
print("Olá {}, bem vindo a disciplina de formatacao. Parabéns pelo seu primeiro hello world".format(nome))

nome = input("DIGITE UM NOME: ")
print(f"OlÁ {nome}, bem vindo a nossa disciplina de formatacao. Parabens pelo seu primeiro hello world") 
#string, 