"""Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento
em uma fábrica, e infirme-o expresso no formato horas:minutos:seguntos.

Entrada     Saída
556         0:9:16

1           0:0:1

140153      38:55:53"""

tempo = int(input())
horas = tempo//3600
aux = tempo%3600
minutos = aux//60
aux = aux%60
segundos = aux%3600

print(f"{horas}:{minutos}:{segundos}")