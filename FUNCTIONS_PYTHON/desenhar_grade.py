#!/usr/bin/env python

def desenhar_grade(linhas, colunas):
    for i in range(linhas * 2 + 1):
        if i % 2 == 0:
            # Linhas horizontais
            print("+", end=" ")
            for j in range(colunas):
                print("- " * 4, end="+ ")
            print()
        else:
            # Linhas verticais
            print("|", end=" ")
            for j in range(colunas):
                print(" " * 7, end=" | ")
            print()

# Solicitar ao usuário a quantidade de linhas e colunas
linhas = int(input("Informe a quantidade de linhas: "))
colunas = int(input("Informe a quantidade de colunas: "))

# Exemplo de uso
desenhar_grade(linhas, colunas)