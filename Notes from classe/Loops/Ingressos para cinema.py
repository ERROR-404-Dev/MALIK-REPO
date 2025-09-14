 # Ingresso de cinema: Um cinema cobra preços diferentes para os ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos de 3 anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o ingresso custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15 dólares. Escreva um laço em que você pergunte a idade aos usuários e, então, informe-lhes o preço do ingresso do cinema.

prompt = '\nQual é sua idade: '

while True:
    Ingresso_idade = int(input(prompt))
    if  Ingresso_idade < 3:
        print('O seu ingresso será gratuito')
    elif Ingresso_idade <= 12:
        print('O seu ingresso custá 10 meticais')
    elif Ingresso_idade > 12:
        print('O seu ingresso custá 15 meticais')
    else:
        print('Wrong input')

