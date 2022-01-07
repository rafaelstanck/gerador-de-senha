"""
Gerador de senha versão 1.0
Senha de 8 dígitos contendo letras minúsculas, maiúsculas, números e caracteres especiais.
teste
"""
from random import choice, randint, shuffle


def gerasenha():

    c1 = r'abcdefghijklmnopqrstuvwxyz0123456789\!@#$%&*+?()[]{}|=/",.;:^_-~'

    senha = [choice(c1[:26]), choice(c1[0:26]).upper(), choice(c1[26:36]), choice(c1[36:])]

    while len(senha) <= 7:
        for i4 in range(1, randint(1, 2)):
            senha.append(choice(c1[36:]))
        for i3 in range(1, randint(1, 2)):
            senha.append(choice(c1[26:36]))
        for i2 in range(1, randint(1, 2)):
            senha.append(choice(c1[:26]).upper())
        for i1 in range(0, (8-len(senha))):
            senha.append(choice(c1[:26]))
    shuffle(senha)
    print(''.join(senha))


gerasenha()
