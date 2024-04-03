"""Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do
produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A*B - C*D).

Entrada     Saída
5           DIFERENCA = -26
6
7
8

0           DIFERENCA = -56
0
7
8

5           DIFERENCA = 86
6
-7
8"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

diferenca = a * b - c * d
print(f"DIFERENCA = {diferenca}")