#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
# caso o valor seja inválido e continue pedindo até que o usuário informe um valor
# válido.

def validarIntervaloDoValor(valor):
    if valor > 0 and valor < 10:
        return True
    else:
        return False


def capturaValor():
    nota = float(input("Informe uma nota entre 0 e 10: "))
    return nota


def main():
    valor = capturaValor()
    condicao = validarIntervaloDoValor(valor)

    while True:
        if not(condicao):
            print("VALOR INVÁLIDO! O valor deve ser um número entre 0 e 10\n")
            valor = capturaValor()
            condicao = validarIntervaloDoValor(valor)
        else:
            break


main()
