from utilidadescev.moeda import moeda
from utilidadescev.dados import validadados

p= validadados.leiaDinheiro('Digite o preço: R$ ')

moeda.resumo (p,200,1)