"""
Gerador de Senha Versão 2.0
Gera senhas de forma customizada, podendo definir a quantidade de letras, números e caracteres especiais.
"""
from random import choice, shuffle


def gerasenha(a=3, b=3, c=3):
    """
    Esta função permite o usuário escolher a quantidade dos caracteres que formarão a senha, sendo:
    a = quantidade de letras (maiúscula ou minúscula)
    b = quantidade de números
    c = quantidade de caracteres especiais
    Colocar o valor 0 (zero) caso não queira letras, números ou caracteres especiais.
    """

    letras = 'ABCDEFGHIJKLMNOPQRSTUVXWYZabcdefghijklmnopqrstuvxwyz'
    numeros = '0123456789'
    caracteres_especiais = r'\|".,;:!@#$%¨&*()+<>?[]{}/-_'
    senha = []

    for i in range(a):  # iterador para acrescentar letras
        senha.append(choice(letras))

    for i in range(b):  # iterador para acrescentar números
        senha.append(choice(numeros))

    for i in range(c):  # iterador para acrescentar caracteres especiais
        senha.append(choice(caracteres_especiais))

    shuffle(senha)  # função para embaralhar os caracteres escolhidos

    return ''.join(senha)  # returna a senha no formato de uma string


senhanova = gerasenha(5, 5, 5)
print(senhanova)
