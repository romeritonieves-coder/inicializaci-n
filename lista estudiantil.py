#realizar un programa que permita leer la edad de n cantidad de estudiantes y muestre un resumen estadístico indicando lo siguiente: 

#1. total de estudiantes ingresados 
#2. ⁠total de estudiantes mayores de edad 
#3. ⁠total de estudiantes entre 18 y 25 años 
#4. ⁠total de estudiantes entre 26 y 30 años 
#5. ⁠total de estudiantes mayores de 30 años
#el programa debe preguntarle al usuario si desea continuar agregando otro estudiante

import os


total = 0  # creamos variable para contener el total de estudiantes 
total_m = 0  # creamos variable para contener el total estudiantes mayores de edad 
total_condicion1 = 0  # creamos variable para contener estudiantes entre 18 y 25 
total_condicion2 = 0  # creamos variable para contener estudiantes entre 26 y 30
total_condicion3 = 0  # creamos variable para contener estudiantes mayores de 30 

while True:
    os.system('cls')
    edad = int(input('Ingresa la edad del estudiante: '))
    total += 1

    match edad:
        case edad if edad < 18:
            pass  

        case edad if 18 <= edad <= 25:
            total_m += 1
            total_condicion1 += 1

        case edad if 26 <= edad <= 30:
            total_m += 1
            total_condicion2 += 1

        case edad if edad > 30:
            total_m += 1
            total_condicion3 += 1

    continuar = input('¿Deseas agregar otro estudiante? (s/n): ')

    match continuar.lower():
        case 's':
            pass  
        case 'n':
            break  
        case _:
            print('Opción no válida, se cerrará el programa.')
            break  


print('\n===== RESUMEN ESTADÍSTICO =====')
print(f'1. Total de estudiantes ingresados:        {total}')
print(f'2. Total de estudiantes mayores de edad:   {total_m}')
print(f'3. Total de estudiantes entre 18 y 25:     {total_condicion1}')
print(f'4. Total de estudiantes entre 26 y 30:     {total_condicion2}')
print(f'5. Total de estudiantes mayores de 30:     {total_condicion3}')



1+1 