achou_maior = False

numeros = [2,4,6,8,10]
for n in numeros:
    if n < 7:
        achou_maior = True
        print(f'{n} é menor que 7')
        #Aqui não colocamos break porque queremos continuar

if achou_maior:
    print('Pelo menos teve um número menor que 7')
else:
    print('Nenhum número menor que 7 foi encontrado')