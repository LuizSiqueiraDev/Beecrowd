"""A fórmula para calcular a área de uma circunferência é: area = n . raio². considerando
para este problema que n = 3.14159:
- Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por n.

Entrada     Saída
2.00        A=12.5664
100.64      A=31819.3103
150.00      A=70685.7750"""

raio = float(input())
n = 3.14159
area = n * (raio * raio)
print(f"A={area:.4f}")