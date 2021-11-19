"""
Gerador de senha versão 1.0
Senha de 8 dígitos contendo letras minúsculas, maiúsculas, números e caracteres especiais.
"""
from random import choice
from random import randint
from random import shuffle


def gerasenha():

    c1, c2, c3, c4 = 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', \
                     '0123456789', r'\!@#$%&*+?()[]{}|=/",.;:^_-~'

    senha = [choice(c1), choice(c2), choice(c3), choice(c4)]

    while len(senha) <= 7:
        for i4 in range(1, randint(1, 2)):
            senha.append(choice(c4))
        for i3 in range(1, randint(1, 2)):
            senha.append(choice(c3))
        for i2 in range(1, randint(1, 2)):
            senha.append(choice(c2))
        for i1 in range(0, (8-len(senha))):
            senha.append(choice(c1))
    shuffle(senha)
    for letra in senha:
        print(letra, end='')


gerasenha()
