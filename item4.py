#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene
# num vetor a média de cada aluno, imprima o número de alunos com média maior
# ou igual a 7.0.


def capturarNotas():
    listaDeNotas = []

    for aluno in range(10):
        print("Informe a nota do aluno ", aluno+1)
        nota = float(input())
        listaDeNotas.append(nota)

    return listaDeNotas


def contarAprovados(listaDeNotas):
    quantidadeAprovados = 0
    for nota in listaDeNotas:
        if(nota >= 7):
            quantidadeAprovados += 1
    return quantidadeAprovados


vetor = [4.0, 5.9, 7.2, 6.0, 10.0, 8.0, 5.0, 6.0, 6.5, 9.0]

print(contarAprovados())
