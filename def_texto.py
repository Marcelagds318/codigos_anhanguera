def aumentar(texto, capslock):
    if capslock:
        return texto.upper()
    else:
        return texto.lower()
texto = aumentar(capslock=False, texto = "REGINALDO")
print(texto)