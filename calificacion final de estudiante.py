'''
realizar un programa que permita leer 4 notas e imprimir nota final 
'''
NOTAEVALUACIONES = 3
NOTAQUIZ = 4
NOTATRABAJOS = 2
notafinal = 0
notaevaluaciones = 0 
notaquiz = 0 
notatrabajos = 0

for i in range(NOTAEVALUACIONES):
    while(True):
        nota = int(input(f'digite nota evaluaciones : [{i+1}] ' ))
        if ((nota >= 0) and (nota <= 100)):
            notaevaluaciones += nota
            break
        else:
            print( ' la nota debe estar en rango de 0 a 100')

for i in range(NOTAQUIZ):
    while(True):
        nota  = int(input(f'digite nota quices : [{i+1}] ' ))
        if ((nota >= 0) and (nota <= 100)):
            notaquiz += nota
            break
        else:
            print( ' la nota debe estar en rango de 0 a 100')

for i in range(NOTATRABAJOS):
    while(True):
        nota = int(input(f'digite nota trabajos : [{i+1}] ' ))
        if ((nota >= 0) and (nota <= 100)):
            notatrabajos += nota
            break
        else:
            print( ' la nota debe estar en rango de 0 a 100')

notafinal = ((notaevaluaciones/NOTAEVALUACIONES)*0.6) + ((notaquiz/NOTAQUIZ)*0.25) + ((notatrabajos/NOTATRABAJOS)*0.15)
print(f'su nota final es de : {notafinal}' )