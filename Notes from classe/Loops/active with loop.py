prompt = 'Diz me algo e eu vou repeti lo: '
prompt += '\nDigite "parar" para acabar o ciclo: '


active = True
while active:
    msg = input(prompt)
    if msg == 'parar':
        active = False
        print('Loop encerrado')
    else:
        print(msg)
    