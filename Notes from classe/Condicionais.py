#Usando condicioanais simples, composto e elif
media = 0.0
n1 = n2 = 0.0

n1 = float(input('Digite tua nota: '))
n2 = float(input('Digite tua nota: '))

#Calculando a média
media = (n1 + n2) / 2

if (media >= 14):
    print('Aprovado, Parabens')
elif (media >= 10):
    print('Recuperação')
else:
    print('Reprovado')

print('Sua media foi {}'.format(media))