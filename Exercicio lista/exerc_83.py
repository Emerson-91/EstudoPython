""" Crie um programa onde o usuario digite uma expressao qualquer que use parenteses, Seu aplicativo devera analisar se
a expressao passada esta com os parenteses aberto e fechados na ordem correta """

expr = str(input('Digite a expressao: '))
p = []
for simb in expr:
    if simb == '(':
        p.append('(')
    elif simb == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
if len(p) == 0:
    print('Sua expressao esta valida!')
else:
    print('Sua expressao esta invalida!')
