#Un centro de salud está realizando una campaña de prevención y necesita un algoritmo que, dado el IMC calculado de un paciente, le indique su **categoría de riesgo**.

#**Reglas:**

#- Si el IMC es menor a 18.5, la categoría es "Bajo peso".
#- Si el IMC es mayor o igual a 18.5 y menor a 25, la categoría es "Peso normal".
#- Si el IMC es mayor o igual a 25 y menor a 30, la categoría es "Sobrepeso".
#- Si el IMC es mayor o igual a 30, la categoría es "Obesidad".

# necesitamos un programa para un centro de salud y dar un resultado segun el riesgo del paciente 

peso = float ( input (' cual es tu peso: '))
altura = float ( input( 'indica tu altura: '))

imc = peso / altura**2
if ( imc < 18.5 ):
    print (f'Bajo de peso, su IMC es de: {round(imc,2)} ')
elif ( imc >= 18.5 and imc < 25):
    print (f'Su peso es normal, su IMC es de: {round(imc,2)} ')
elif ( imc >= 25 and imc < 30):
    print (f'Sobrepeso, su IMC es de: {round(imc,2)} ')
else :
    print (f'Obesidad, su IMC es de: {round(imc,2)} ')
    