alunos = [
    {'nome' : 'Yasmin', 'notas' : [8, 7], 'idade' : 16, 'faltas': 367},
    {'nome' : 'Bruno', 'notas' : [8, 7], 'idade' : 16, 'faltas': 54}
    ]

def calcular_media(soma, qtde):
    return soma / qtde

def status_presenca(num_faltas):
    if num_faltas < 300:
        return('Dentro do limite')
    else:
        return('Fora do limite de faltas')

def status_aprovacao(nota, num_faltas):
    if nota >= 7 and num_faltas < 300:
        return('Aprovado')
    else:
        return('Reprovado')


for aluno in alunos:
    qtde_notas = len(aluno['notas'])
    soma = sum(aluno['notas'])

    nota = calcular_media(soma, qtde_notas)
    print(f"Aluno: {aluno['nome']}, Nota: {nota}, Status: {status_aprovacao(nota, aluno['faltas'])}, Faltas: {status_presenca(aluno['faltas'])}")