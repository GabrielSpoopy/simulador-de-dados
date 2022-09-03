import random, time

def main(): 
    print('Simulador de dados')
    ladosDado = input('qual vai ser a quantidade de lados do dado que voce vai jogar? ')
    if ladosDado.isnumeric():
        print('rolando...')
        time.sleep(1)
        print(f'o resultado da rolagem é {random.randint(1, int(ladosDado))}')
    else:
        print('parece que isso não é um numero, veja se voce escreveu certo \n')
        main()
    

main()