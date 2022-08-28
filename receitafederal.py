salario = 0 #variavel com valor zero
salario = float(input("DIGITE O SALARIO DO COLABORADOR: R$  ")) #string convertido em float com entrada
if salario <=1903.98: #se o salario for menor ou igual a 
    print(f"O COLABORADOR ESTÁ ISENTO DE IMPOSTO.\nO desconto é de: R$00,00") #mostrar ao usuario
elif salario >1903.98 and salario <=2826.65: #else if o salario for entre dois valores
    slr= salario-142.80 #subtração da taxa de impostos, slr é convertido em float
    salr = "{:.2f}".format(slr) # converte salario em float
    salari = str(salr) #converse salr em float mostra ao colaborador o valor
    dsc = salario-(salario-142.8) #peracao do valor q o colaborador vai pagar de salario
    dsct = "{:.2f}".format(dsc) #convert dsc em float
    dscnt = str(dsct) #convert dsct em string para mostrar ao colaborador o desconto
    print(f"O COLABORADOR DEVE PAGAR: {dscnt} DE IMPOSTO.\nValor do salário líquido: R$: "+ salari ) #o salario é mostrado ao colaborador e o n\ quebra a linha
elif salario >2826.65 and salario <=3751.05:
    slr2= salario-354.80
    salr2 =  "{:.2f}".format(slr2) 
    salari2 = str(salr2)
    dsc2 = salario-(salario-354.80)
    dsct2 = "{:.2f}".format(dsc2)
    dscnt2 = str(dsct2)
    print(f"O COLABORADOR DEVE PAGAR: {dscnt2} DE IMPOSTO.\nValor do salário líquido: R$: "+ salari2 )
elif salario >3751.05 and salario <=4664.68:
    slr3= salario-636.13
    salr3 = "{:.2f}".format(slr3)
    salari3 = str(salr3)
    dsc3 = salario-(salario-636.13)
    dsct3 = "{:.2f}".format(dsc3)
    dscnt3 = str(dsct3)
    print(f"O COLABORADOR DEVE PAGAR: {dscnt3} DE IMPOSTO.\nValor do salário líquido: R$: "+ salari3 )
elif salario >4664.68:
    slr4= salario-869.36
    salr4 = "{:.2f}".format(slr4)
    salari4 = str(salr4)
    dsc4 = salario-(salario-869.36)
    dsct4 = "{:.2f}".format(dsc4)
    dscnt4 = str(dsct4)
    print(f"O COLABORADOR DEVE PAGAR: {dscnt4} DE IMPOSTO.\nValor do salário líquido: R$: "+ salari4 )
