#4 Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1, nota2, nota3, nota4 = map(float, input("Digite quatro notas: ").split())
media = (nota1 + nota2 + nota3 + nota4)/4
print("A média é ", media)
