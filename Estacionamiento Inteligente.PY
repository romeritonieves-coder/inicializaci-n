#Un parqueadero automatizado cobra tarifas diferenciadas según el tiempo de permanencia. El objetivo es calcular el **total a pagar** según la cantidad de horas que el vehículo estuvo estacionado.

#**Reglas:**

#- Para estancias de hasta 2 horas (menor o igual), la tarifa es fija de $3.000.
#- Para estancias mayores a 2 horas y menores o iguales a 5 horas, la tarifa es de $2.000 por hora adicional.
#- Para estancias superiores a 5 horas, se cobra una tarifa plena de $15.000 por todo el día.

# NECESITAMOS CREAR un programa que nos calcule el precio total apagar bpor el tiempo que estuvo un carro estacionado en un parqueadero 

hora = int ( input ( ' digite el tiempo en horas que estuvo el carro estacionado: '))

tarifa_f = 3000
if ( hora <= 2 ):
    print ( f'su tiuempo en el estacionamiento fue de: {hora}h, y su total a pagar es de {tarifa_f}')
elif ( hora > 2 and hora <= 5 ):
    total_p = tarifa_f + (( hora - 2 )* 2000)
    print ( f' su tiuempo en el estacionamiento fue de: {hora}h, y su total a pagar es de {total_p}' )
else : 
    print ( f' su tiuempo en el estacionamiento fue de: {hora}h, y su total a pagar es de 15.000' )