prompt = 'Diz me algo e eu vou repeti lo: '
prompt += '\nDigite "parar" para acabar o ciclo\n'

message = ''
while message != 'parar':
    message = input(prompt)
    print('\n',message)