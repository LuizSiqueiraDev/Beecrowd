"""Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor
unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor únitário
de cada peça 2. Após, calcule e mostre o valor a ser pago.

Entrada         Saída
12 1 5.30       VALOR A PAGAR: R$ 15.50
16 2 5.10

13 2 15.30      VALOR A PAGAR: R$ 51.40
161 4 5.20

1 1 15.10       VALOR A PAGAR: R$ 30.20
2 1 15.10"""

codigo_1, qtd_1, valor_1 = map(float, input().split())
codigo_2, qtd_2, valor_2 = map(float, input().split())

total = float((qtd_1 * valor_1) + (qtd_2 * valor_2))
print(f"VALOR A PAGAR: R$ {total:.2f}")