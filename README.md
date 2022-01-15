# Calculo-Salario-Horista
Programa para estimar o salário liquido e bruto de um trabalhador horista sob regime CLT

# Introdução

Frequentemente trabalhadores em regime CLT que recebem por hora tem dificuldades de compreender e estimar com clareza o salario final em função do salario base e das horas trabalhadas. Esse programa tem a finalidade de elaborar os calculos e estimar o salario liquido e bruto em função das horas trabalhadas e do salario base, bem como os descontos. 

Esse programa não substitui o trabalho de um contador, é apenas uma referência para ajudar o trabalhador horista a estimar seu salario e compreender melhor seu holerite.

# Uso

Chamar a classe 'salario_horista' e passar os argumentos:
  - hora_aula: Valor da hora de trabalho
  - horas_trabalhadas: Quantidade de horas trabalhadas no mes
  - extras: Adicionais tributaveis que eventualmente incidem no mes (lista)
  - hora_atividade: Proporcao a ser acrescentada nas horas trabalhadas

As informações são compiladas em um DataFrame (Pandas) contendo os salarios liquidos e bruto, bem como os descontos relativos a imposto de renda e INSS

A função 'exemplo' descreve um uso tipico

# Função 'Liquido2Horas'

Essa função tem o objetivo de estimar quantas horas de trabalho são necessarias para conseguir um determinado salário liquido em função do valor recebido por hora trabalhada

# Observações

É necessário atualizar as faixas salariais relativas aos descontos de INSS e imposto de renda

