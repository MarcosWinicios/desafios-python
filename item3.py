#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Faça uma função que calcule a média de um aluno de acordo com o critério
# definido neste curso. Além disso, faça uma segunda função que informe o status
# do aluno de acordo com a tabela a seguir: Nota acima de 6 à “Aprovado” Nota
# entre 4 e 6 à Conceito “Verificação Suplementar” Nota abaixo de 4 à Conceito
# “Reprovado”

def calcularMedia(nota1, nota2):
    media = (nota1 + nota2)/2
    return media


media = calcularMedia(6, 8)
print(media)
