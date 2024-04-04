"""Faça um programa que leia três valores a apresente o maior dos três valores lidos
seguido da mensagem 'eh o maior'. Utilize a fórmula:

MaiorAB = (a+b+abs(a-b))/2

Obs: A fórmula apensa calcula o maior entre os dois primeiros (a e b). Um segundo passo,
portanto é necessário para chegar no resultado esperado.

Entrada     Saída
7 14 106    106 eh o maior

217 14 6    217 eh o maior"""

a, b, c = map(int, input().split())
maior = max(a, b, c)
print(f"{maior} eh o maior")