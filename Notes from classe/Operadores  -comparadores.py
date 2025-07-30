# Código com o operador AND
idade = 18
altura = 1.75

resultado = (idade >= 18) and (altura >= 1.75)
msg = 'Pode participar do evento? ' + str(resultado)
print(msg)

#Código para OR com disparo de alarme
porta = 'f'
janela = 'f'

resultado = (porta == 'a') or (janela == 'a')
msg = 'Alarme disparado ?' + str(resultado)
print(msg)

#Inverter o estado lógico
tem_dinheiro = False
tem_dinheiro = not tem_dinheiro
print('Tem dinheiro? ' + str(tem_dinheiro))