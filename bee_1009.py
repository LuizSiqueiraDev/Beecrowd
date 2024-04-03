"""Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de
vendas efetuadas por ele no mês(em dinheiro). Sabendo que este vendedor ganha 15% de
comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com
duas casas decimais.

Entrada     Saída
JOAO        TOTAL = R$ 684.54
500.00
1230.30

PEDRO       TOTAL = R$ 700.00
700.00
0.00

MANGOJATA   TOTAL = R$ 1884.58
1700.00
1230.50"""

nome = str(input())
salario = float(input())
vendas = float(input())
total = salario + (vendas * 0.15)
print(f"TOTAL = R$ {total:.2f}")