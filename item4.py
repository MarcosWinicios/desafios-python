#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene
# num vetor a média de cada aluno, imprima o número de alunos com média maior
# ou igual a 7.0.

def calcularMedia(listaDeNotas):
    media = 0
    soma = 0
    for nota in listaDeNotas:
        soma += nota
    media = soma / len(listaDeNotas)

    return media


def capturaNotasIndividuais(aluno):
    listaDeNotas = []
    for nota in range(4):
        print("Informe a ", nota+1, "° nota do aluno ", aluno+1, " :")
        valor = float(input())
        listaDeNotas.append(valor)
    return listaDeNotas


def capturarNotasDeTodosAlunos():
    listaDeMedias = []

    for aluno in range(10):
        media = calcularMedia(capturaNotasIndividuais(aluno))
        print("Média: ", media)
        print("\n___________________________\n")
        listaDeMedias.append(media)

    return listaDeMedias


def contarAprovados(listaDeNotas):
    quantidadeAprovados = 0
    for nota in listaDeNotas:
        if(nota >= 7):
            quantidadeAprovados += 1
    return quantidadeAprovados


def main():
    listaDeMedias = capturarNotasDeTodosAlunos()
    quantidadeAprovados = contarAprovados(listaDeMedias)
    print(quantidadeAprovados)


main()

vetor = [4.0, 5.9, 7.2, 6.0, 10.0, 8.0, 5.0, 6.0, 6.5, 9.0]

print(contarAprovados())
