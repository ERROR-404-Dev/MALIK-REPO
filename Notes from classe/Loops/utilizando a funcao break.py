prompt = '\nColoque nome de uma cidade que ja visitou'
prompt += '\nDigite "parar" para encerrar as perguntas: '

while True:
    msg = input(prompt)
    if msg == 'parar':
        break
    else:
        print(msg)