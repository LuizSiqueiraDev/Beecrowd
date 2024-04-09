"""Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em
anos, meses e dias.

Obs: apenas para facilitar o cálculo, considere todo ano com 356 dias e todo mês com 30
dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias,
como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio 
matemático simples.

Entrada     Saída
400         1 ano(s)
            1 mes(s)
            5 dia(s)

800         2 ano(s)
            2 mes(s)
            10 dia(s)

30          0 ano(s)
            1 mes(s)
            0 dia(s)"""

tempo = int(input())

ano = tempo//365
aux = tempo%365

mes = aux//30
aux = aux%30

dia = aux%30

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")