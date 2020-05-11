""" Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um
dicionario se por acaso a CTPS for diferente de zero, o dicionario receberá tambem o ano de contrataçao e o salario.
Calcule e acrescente a idade, alem da idade com quantos anos a pessoa vai se aposentar.
CONSEIDERAR 35 ANOS DE CONTRIBUICAO"""
from datetime import date
pessoa = dict()
pessoa['nome'] = str(input("Informe o nome: "))
nascimento = int(input("Informe o ano de nascimento: "))
anoatual = date.today().year
pessoa['idade'] = anoatual - nascimento
ctps = int(input("Carteira de trabalho (0 nao tem): "))

if ctps == 0:
    for k,v in pessoa.items():
        print(f'{k} tem o valor {v}')
elif ctps > 0:
    pessoa['contratacao'] = int(input("Ano de contrataçao: "))
    pessoa['salario'] = float(input("Salário: "))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratacao']+ 35) - anoatual)
    for k, v in pessoa.items():
        print(f'{k} tem o valor de {v}')
else:
    print("o Valor nao pode ser NEGATIVO")











#print(pessoa['idade'])