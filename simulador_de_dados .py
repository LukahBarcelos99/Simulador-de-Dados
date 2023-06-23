#Criando um simulador de dados!
import random

class SimuladorDeDados:
    def __init__(self, ladoInicial, qtdeLado):
        print('BEM-VINDO AO SIMNULADOR DE DADOS!')
        self.ladoInicial = ladoInicial
        self.qtdeLado = qtdeLado


qtde_lado = input('Digite a quantidade de lados que seu dado precisa ter: ')
dado = SimuladorDeDados.qtdeLado(0, qtde_lado)
ladoInicial = SimuladorDeDados.ladoInicial(1)
print('Você optou por usar um D', dado)

simulacao = random.randint(ladoInicial, dado)

print('Resultado é: ', simulacao)


