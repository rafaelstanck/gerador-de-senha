"""
Gerador de senha versão 1.0
Senha de 8 dígitos contendo letras minúsculas, maiúsculas, números e caracteres especiais.
"""
from random import choice
from random import randint
from random import shuffle

ca1 = 'abcdefghijklmnopqrstuvwxyz'
ca2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ca3 = '0123456789'
ca4 = r'\!@#$%&*+?()[]{}|=/",.;:^_-~'

senha = [choice(ca1), choice(ca2), choice(ca3), choice(ca4)]

while len(senha) <= 7:
    for i4 in range(1, randint(1, 2)):
        senha.append(choice(ca4))
    for i3 in range(1, randint(1, 2)):
        senha.append(choice(ca3))
    for i2 in range(1, randint(1, 2)):
        senha.append(choice(ca2))
    for i1 in range(0, (8-len(senha))):
        senha.append(choice(ca1))
shuffle(senha)
for letra in senha:
    print(letra, end='')
