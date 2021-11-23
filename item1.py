#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Faça um programa com uma função chamada somaImposto. A função possui dois
# parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas
# expressa em porcentagem e custo, que é o custo de um item antes do imposto. A
# função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    taxaImposto = taxaImposto/100
    imposto = custo * taxaImposto
    return imposto + custo


def capturarDados():
    custoItem = float(input("Iforme o custo do item: "))
    taxaImposto = float(input("Iforme a taxa de imposto deste item: "))
    return custoItem, taxaImposto


def main():
    custoItem, taxaImposto = capturarDados()
    valorTotal = somaImposto(taxaImposto, custoItem)
    print("\nValor total do produto para venda: R$ %.2f" % valorTotal)


main()
