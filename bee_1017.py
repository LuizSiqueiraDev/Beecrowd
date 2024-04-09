"""Joanzinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma
viagem, ao utilizar um automóvel que faz 12 km/l. Para isso, ele gostaria que você o auxiliasse
através de uma simples programa. Para efetuar o cálculo, deve-se fornecer o tempo gasto
na viagem (em horas) e a velocidade média durante a mesma (em km/l). Assim, pode-se obter
distância percorrida e, em seguida, calcular quantos litros seriam necessários. Mostre o
valor com 3 casas decimais após o ponto.

Entrada     Saída
10          70.833
85

2           15.333
92

22          122.833
67"""

tempo = int(input())
velocidade = int(input())

litros = (velocidade * tempo) / 12
print(f"{litros:.3f}")