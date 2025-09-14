achou_maior = False

numero = [2,4,6,8,10]
for n in numero:
    if n > 7:
        achou_maior = True
        print(f'{n} é maior que 7')
        #Aqui nao colocamos break porque queremos continuar
if achou_maior:
    print('Pelo menos tem um número maior que 7')
else:
    print('Nenhum número maior que 7 foi encontrado')