#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def contarDigitos(numero):
    return len(str(numero))


def main():
    numero = int(
        input("Informe um número para saber a quantidade de dígitos: \n"))
    print(contarDigitos(numero), " dígitos")


main()
