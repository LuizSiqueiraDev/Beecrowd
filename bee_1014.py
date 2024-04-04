"""Calcule o consumo médio de automóvel sendo fornecidos a distância total percorrida
(em km) e o total de combustível gasto (em litros).

Entrada     Saída
500         14.286 km/l
35.0

2254        18.119 km/l
124.4

4554        9.802 km/l
464.6"""

distancia = int(input())
combustivel = float(input())

gasto = distancia / combustivel
print(f"{gasto:.3f} km/l")