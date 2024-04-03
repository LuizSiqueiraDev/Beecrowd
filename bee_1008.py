"""Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas,
o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o 
número e o salário do funcionário, com duas casas decimais.

Entrada     Saída
25          NUMBER = 25
100         SALARY = U$ 500.00
5.50

1           NUMBER = 1
200         SALARY = U$ 4100.00
20.50

6           NUMBER = 6
145         SALARY = U$ 2254.75
15.55"""

numero = int(input())
horas = int(input())
valor = float(input())

salario = horas * valor
print(f"NUMBER = {numero}")
print(f"SALARY = U$ {salario:.2f}")