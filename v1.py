"""
Gerador de senha versão 1.0
Senha de 8 dígitos contendo letras minúsculas, maiúsculas, números e caracteres especiais.
"""
from random import choice, randint, shuffle


def gerasenha():

    caracter = r'abcdefghijklmnopqrstuvwxyz0123456789\!@#$%&*+?()[]{}|=/",.;:^_-~'  # caracteres a serem utilizados

    senha = [choice(caracter[:26]), choice(caracter[0:26]).upper(), choice(caracter[26:36]), choice(caracter[36:])]

    while len(senha) <= 7:
        for i4 in range(1, randint(1, 2)):
            senha.append(choice(caracter[36:]))
        for i3 in range(1, randint(1, 2)):
            senha.append(choice(caracter[26:36]))
        for i2 in range(1, randint(1, 2)):
            senha.append(choice(caracter[:26]).upper())
        for i1 in range(0, (8-len(senha))):
            senha.append(choice(caracter[:26]))
    shuffle(senha)
    print(''.join(senha))


gerasenha()
