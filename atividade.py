def minha_funcao(valor):
    for i, c in enumerate(valor):
        if c.lower() == "a" or c.lower() == "e":
            print(c, i)
        else:
            continue
rosa = minha_funcao("era uma vez uma abelha bem bonita E ROSA VOCE TINHA QUE VER")
print(rosa)