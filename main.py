import random, time

class SimuladorDados:
    def __init__(self):
        print('Simulador de dados! \n')
        self.dadosLados = int(input('qual vai ser a quantidade de lados do dado que voce vai rolar? '))

    def getRandomNumber(self):
        return random.randint(1, self.dadosLados)

    def iniciar(self):
        resultado = self.getRandomNumber()
        print('rolando...')
        time.sleep(1)
        print(f'o resultado da rolagem foi {resultado}')
        
simularDados = SimuladorDados()
simularDados.iniciar()
