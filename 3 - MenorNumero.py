num = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

# for i in lista (0,3):

if (num > num2) and (num > num3):
    teste = num
    num = num3
    num3 = teste

if (num2 > num) and (num2 > num3):
    teste = num2
    num2 = num3
    num3 = teste

if (num > num2) and (num2 < num3):
    teste = num
    num = num2
    num2 = teste

print('O menor número é:  {}'.format(num))
