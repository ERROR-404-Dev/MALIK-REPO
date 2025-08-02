senha = 1234
idade_minima = 18
print(f'A senha é {senha}')
Senha_input = int(input('Digite a senha:' ))


if (Senha_input == senha) :
    Idade = int(input('Digite sua idade:' ))
    if (Idade >= idade_minima):
        print('Tens acesso ao site')
    else:
        print('Infelizmente não tens acesso ao site és menor de idade')
else:
    print('Senha incorreta')