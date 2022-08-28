disciplina = "INGLES"
for c in disciplina:
    if c == 'a': #se uma das letras da disciplina digitada for A, parar o laço
        break #quando chegou a primeira letra a, a estrutura de repetição foi interrompida.  "pular" algumas execuções, dependendo de uma condição. condicao c==A parar
    else:
        print(c)