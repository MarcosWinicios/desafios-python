#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene
# num vetor a média de cada aluno, imprima o número de alunos com média maior
# ou igual a 7.0.
def validarIntervalo(entrada):
    if entrada >= 0 and entrada <= 10:
        return True
    else:
        return False


def validarValor(nota):
    condicao = validarIntervalo(nota)
    while True:
        if not(condicao):
            print("\n>>>> VALOR INVÁLIDO! A nota deve ser um valor dede 0 e 10 <<<<\n")
            nota = float(input("Iforme uma nota válida: "))
            condicao = validarIntervalo(nota)
        else:
            print("\n")
            break

    return nota


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
        valor = validarValor(valor)
        listaDeNotas.append(valor)

    print("\nNotas: ", listaDeNotas, "\n")
    return listaDeNotas


def capturarNotasDeTodosAlunos():
    listaDeMedias = []

    for aluno in range(10):
        media = calcularMedia(capturaNotasIndividuais(aluno))
        print("Média: %.1f" % media)
        print("\n_____________________________________________\n")
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
    print(">>>> RESULTADO FINAL <<<\n\nLista de médias:\n\n", listaDeMedias, "\n\nQuantidade de alunos aprovados: ",
          quantidadeAprovados, ".\nEstes obtiveram média MAIOR OU IGUAL a 7")


main()
