"""Leia um valor de ponto flutuante com duas casas decimais. Este valor representa
um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no 
qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2.
As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação
de notas necssárias.

Entrada     Saída
576.73      NOTAS:
            5 nota(s) de R$ 100.00
            1 nota(s) de R$ 50.00
            1 nota(s) de R$ 20.00
            0 nota(s) de R$ 10.00
            1 nota(s) de R$ 5.00
            0 nota(s) de R$ 2.00
            MOEDAS:
            1 moeda(s) de R$ 1.00
            1 moeda(s) de R$ 0.50
            0 moeda(s) de R$ 0.25
            2 moeda(s) de R$ 0.10
            0 moeda(s) de R$ 0.05
            3 moeda(s) de R$ 0.01"""

reais, centavos = map(int, input().split('.'))
centavos = centavos + reais*100

notas = [100,50,20,10,5,2]

print('NOTAS:')
for nota in notas:
    print(f"{centavos//(nota*100)} nota(s) de R$ {nota}.00")
    centavos = centavos%(nota*100)

moedas = [100,50,25,10,5,1]

print('MOEDAS:')
for moeda in moedas:
    print(f"{centavos//moeda} moeda(s) de R$ {moeda//100}.{moeda%100:02}")
    centavos = centavos%moeda