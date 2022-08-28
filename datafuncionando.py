def converte_mes (data):
    mes = '''Janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'''.split()
    d,m,a = data.split('/')
    mes_extenso = mes[int(m)-1]
    return f'{d} de {mes_extenso} de {a}'
print(converte_mes('10/05/2021'))