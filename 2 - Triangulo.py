a = int('Digite o valor de A: '))
b = int('Digite o valor de B: '))
c = int('Digite o valor de C: '))

import math

if a>(b+c):
	print ('se A > B + C nao e possivel formar triangulo,se A eh maior')

else:
 lado = (a+b+c) / 2
area = perimetro * (perimetro - a) * (perimetro - b) * (perimetro -c)
areaf = math sqrt(area)
print ( 'a area do triangulo eh:' , areaf)