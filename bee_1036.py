"""Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara.
Se não for possível calcular as raízes, mostre a mensagem correspondente 'Impossivel
calcular', caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada         Saída
10.0 20.1 5.1   R1 = -0.29788
                R2 = -1.71212

0.0 20.0 5.0    Impossivel calcular

10.3 203.0 5.0  R1 = -0.024466
                R2 = -19.68408

10.0 3.0 5.0    Impossivel calcular"""

import math

a,b,c = map(float, input().split())

d = (b**2) - (4*a*c)

if d < 0 or a == 0:
    print("Impossivel calcular")
else:
    d = math.sqrt(d)
    r1 = (-b+d) / (2*a)
    r2 = (-b-d) / (2*a)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")
