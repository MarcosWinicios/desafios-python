#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def validarValor(valor):
    if valor > 0 and valor < 10:
        return True
    else:
        return False


def main(valor):
    condicao = validarValor(valor)
    while True:
        if not(condicao):
            print("VALOR INVÁLIDO! O valor deve ser um número entre 0 e 10\n")
            nota = int(input("Informe uma nota entre 0 e 10: \n"))
            condicao = validarValor(nota)
        else:
            break


nota = int(input("Informe um valor entre 0 e 10: \n"))
main(nota)
