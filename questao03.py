#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Faça uma função que calcule a média de um aluno de acordo com o critério
# definido neste curso. Além disso, faça uma segunda função que informe o status
# do aluno de acordo com a tabela a seguir: Nota acima de 6 à “Aprovado” Nota
# entre 4 e 6 à Conceito “Verificação Suplementar” Nota abaixo de 4 à Conceito
# “Reprovado”

def calcularMedia(nota1, nota2):
    media = 0
    media = (nota1 + nota2)/2
    return media


def definirStatus(nota):
    status = ''
    if nota > 6:
        status = "Aprovado"
    elif nota > 4:
        status = "Verificação Suplementar"
    else:
        status = "Reprovado"

    return status


def validarIntervaloValor(entrada):
    if entrada >= 0 and entrada <= 10:
        return True
    else:
        return False


def validarEntrada(nota):
    condicao = validarIntervaloValor(nota)

    while True:
        if not(condicao):
            print("VALOR INVÁLIDO! A nota deve ser um valor entre 0 e 10\n")
            nota = float(input("\nIforme uma nota válida: "))
            condicao = validarIntervaloValor(nota)
        else:
            break
    return nota


def main():
    print("Informe a primeira nota: ")
    nota1 = float(input())
    nota1 = validarEntrada(nota1)
    print("Informe a segunda nota: ")
    nota2 = float(input())
    nota2 = validarEntrada(nota2)
    print("\n")

    media = calcularMedia(nota1, nota2)
    status = definirStatus(media)
    print("Média do aluno: ", media)
    print("Status do aluno: ", status)


main()
