"""Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas)
no qual o valor pode ser decomposto. As notas consideradas são dde 100, 50, 20, 10, 5,
2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada     Saída
576         576
            5 nota(s) de R$ 100,00
            1 nota(s) de R$ 50,00
            1 nota(s) de R$ 20,00
            0 nota(s) de R$ 10,00
            1 nota(s) de R$ 5,00
            0 nota(s) de R$ 2,00
            1 nota(s) de R$ 1,00
            
11257       11257
            112 nota(s) de R$ 100,00
            1 nota(s) de R$ 50,00
            0 nota(s) de R$ 20,00
            0 nota(s) de R$ 10,00
            1 nota(s) de R$ 5,00
            1 nota(s) de R$ 2,00
            0 nota(s) de R$ 1,00
            
503         503
            5 nota(s) de R$ 100,00
            0 nota(s) de R$ 50,00
            0 nota(s) de R$ 20,00
            0 nota(s) de R$ 10,00
            0 nota(s) de R$ 5,00
            1 nota(s) de R$ 2,00
            1 nota(s) de R$ 1,00"""

n = int(input())
n100 = n//100
aux = n%100
n50 = aux//50
aux = aux%50
n20 = aux//20
aux = aux%20
n10 = aux//10
aux = aux%10
n5 = aux//5
aux = aux%5
n2 = aux//2
aux = aux%2
n1 = aux//1
aux = aux%1

print(n)
print(f"{n100} nota(s) de R$ 100,00")
print(f"{n50} nota(s) de R$ 50,00")
print(f"{n20} nota(s) de R$ 20,00")
print(f"{n10} nota(s) de R$ 10,00")
print(f"{n5} nota(s) de R$ 5,00")
print(f"{n2} nota(s) de R$ 2,00")
print(f"{n1} nota(s) de R$ 1,00")