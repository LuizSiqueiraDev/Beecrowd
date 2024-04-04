"""Faça um programa que calcule e mostre o valume de uma esfera sendo fornecido o valor
de seu raio (R). A fórmula para calcular o volume é: (4/3) * pi * R³.
Considere(atribua) para pi o valor 3.14159.

Dica: Ao utilizar a fórmula, procure usar (4/3.0) ou (4.0/3), pois algumas linguagens
(dentre elas o C++), assumem que o resultado da divisão entre dois inteiros é outro
inteiro.

Entrada     Saída
3           VOLUME = 113.097

15          VOLUME = 14137.155

1523        VOLUME = 14797486501.627"""

r = float(input())
volume = (4.0/3) * 3.14159 * r**3
print(f"VOLUME = {volume:.3f}")