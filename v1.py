"""
Gerador de senha versão 1.0
Senha de 8 dígitos contendo letras minúsculas, maiúsculas, números e caracteres especiais.
"""
from random import choice, randint, shuffle


def gerasenha():

    c1, c2, c3 = 'abcdefghijklmnopqrstuvwxyz', '0123456789',\
                     r'\!@#$%&*+?()[]{}|=/",.;:^_-~'

    senha = [choice(c1), choice(c1).upper(), choice(c2), choice(c3)]

    while len(senha) <= 7:
        for i4 in range(1, randint(1, 2)):
            senha.append(choice(c3))
        for i3 in range(1, randint(1, 2)):
            senha.append(choice(c2))
        for i2 in range(1, randint(1, 2)):
            senha.append(choice(c1).upper())
        for i1 in range(0, (8-len(senha))):
            senha.append(choice(c1))
    shuffle(senha)
    print(''.join(senha))


gerasenha()
