#Sintaxte do print

#Print(objeto , argumento)
nome = input('Digite seu nome: ')
msg = 'Olá' + nome + '! Bem-vindo ao curso de Python!'
print(msg)

#Para fazer quebra de linha

print('Essa mensagem continua e permanece na mesma linha.', end='')
print(' E vai continuar nessa linha')

#Para fazer mensagem formatada
nome = 'Malik'
idade = '17'
msg_formatada = 'O seu nome é {0} e a sua idade é {1}'.format(nome,idade)
print(msg_formatada)

#Formatar string

nome = 'Rogério'
peso = 67.7
altura = 1.27
msg = f'Olá {nome} o seu peso é {peso} e a tua altura é {altura}'
print(msg)

#Formatar string com fórmula
a = 2
b = 3
res = f'A soma de {a} + {b} = {a+b}'
print(res)

#Formatar com float
valor = 123.8383883
print(f'O valor é{valor:.2f}')