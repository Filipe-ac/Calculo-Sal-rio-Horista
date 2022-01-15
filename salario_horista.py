from fplot3 import *
from scipy.interpolate import interp1d


def calc_inss(salario):
    '''funcao para calcular o inss total'''

    #atualizar as aliquotas aqui
    cota = [7.5,9,12,14,0] #porcentagem do imposto
    lista = [0,1100,2203.48,3305.22,6433.57,np.inf] #faixas salariais
    
    irrf = 0
    for i in range(len(lista)-1):
        
        if salario >= lista[i]:
            if salario >= lista[i+1]:
                aliquota = lista[i+1] - lista[i]
            else:
                aliquota = salario - lista[i]
            irrf += aliquota*cota[i]/100
        else:
            return irrf
    return irrf

def calc_irrf(salario):
    '''funcao para calcular o imposto de renda'''

    #atualizar as aliquotas aqui
    cota = [0,7.5,15,22.5,27.5] #porcentagem do imposto
    lista = [0,1903.99,2826.65,3751.05,4664.69] #faixas salariais

    irrf = 0
    for i in range(len(lista)-1):
        if salario >= lista[i]:
            if salario >= lista[i+1]:
                aliquota = lista[i+1] - lista[i]
            else:
                aliquota = salario - lista[i]
            irrf += aliquota*cota[i]/100
        else:
            return irrf
    return irrf
        
class salario_horista:
    def __init__(self,hora_aula,horas_trabalhadas,
                 extras = [],
                 hora_atividade = 0.05):

        '''hora_aula: valor da hora de trabalho
           horas_trabalhadas: horas trabalhadas durante o mes
           extras: adicionais (lista)
           hora_atividade: adicional de hora atividade (proporcao)'''
        
        self.ha = hora_aula
        self.hora_atividade = hora_atividade
        self.fgts = 0.08

        self.dsr = 1/6

        horas_aula = hora_aula*horas_trabalhadas
        bruto = horas_aula*(1+self.hora_atividade) + sum(extras)
        bruto *= (1 + self.dsr)
        inss = calc_inss(bruto)
        fgts = bruto*self.fgts
        base_irrf = bruto - inss
        irrf = calc_irrf(base_irrf)
        liquido = bruto - irrf - inss

        self.dict = {'horas aula':horas_aula,
                     'hora atividade': horas_aula*(1+self.hora_atividade),
                     'bruto': bruto,
                     'inss': inss,
                     'fgts': fgts,
                     'irrf': irrf,
                     'liquido': liquido}
       
        self.df = pd.Series(self.dict)

        self.total = self.df.liquido + self.df.fgts + \
        (self.df.liquido/3)/12 + self.df.liquido/12


def Liquido2Horas(salario_liquido,salario_base):
    '''Retorna quantas horas de trabalho sao necessarias para receber
        o valor salario_liquido dado o valor do salario_base'''

    #funcao para aplicar na minimizacao
    def func2(horas):
        return salario_horista(salario_base,horas).df.liquido
    
    from scipy.optimize import minimize
    #usar algoritmo de minimizacao para encontrar as horas necessarias
    horas = minimize(lambda x: abs(func2(x) - salario_liquido),60)

    return horas.x[0]

    



def exemplo():
    salario_base = 40 # 43.65 por hora de trabalho
    horas_trabalhadas = 80 # horas trabalhadas no mes
    sal = salario_horista(salario_base,horas_trabalhadas)
    print('Salario liquido, bruto e descontos:')
    print(sal.df.round(2))

    salario_esperado = 5000
    print('\nFuncao para estimar as horas trabalhadas dado o salario liquido:')
    print('Horas necessarias: %s'%round(Liquido2Horas(salario_esperado,salario_base),2))
    

#exemplo()
