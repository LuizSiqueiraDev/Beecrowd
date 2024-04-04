"""Escreva um progama que leia três valores com ponto flutuante de dupla precisão:
A, B e C. Em seguida, calcule e mostre:

A) a área do triângulo retângulo que tem A por base e C por ALtura.
B) a área do círculo de raio C.(pi=3.14159)
C) a área do trapézio que tem A e B por base e C por altura.
D) a área do quadrado que tem lado B.
E) a área do retângulo que tem lados A e B.

Entrada         Saída
3.0 4.0 5.2     TRIANGULO: 7.800
                CIRCULO: 84.949
                TRAPEZIO: 18.200
                QUADRADO: 16.000
                RETANGULO: 12.000

12.7 10.4 15.2  TRIANGULO: 7.800
                CIRCULO: 84.949
                TRAPEZIO: 18.200
                QUADRADO: 16.000
                RETANGULO: 12.000"""

a, b, c = map(float, input().split())
triangulo = (a * c) * 1/2
circulo = 3.14159 * c**2
trapezio = ((a+b) * c) / 2
quadrado = b*b
retangulo = a*b

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")