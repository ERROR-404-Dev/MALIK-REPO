x = y = z = False
n1 = n2 = 0

print('Digite um número: ')
n1 = int(input())
n2 = int(input('Digite outro número: '))

x = n1 == n2
print('São iguais ?', x)

y = n1 <= n2
print(n1,'é menor ou igual a', n2,'? ', y,'\n' )

z = n1 != n2
print('São diferentes ?'+ str(z), '\n')