# Ejercicio Bonificación de Empleados

#El departamento de Recursos Humanos de una empresa de tecnología desea calcular el **porcentaje de bono** anual que le corresponde a sus empleados basándose en su antigüedad (años trabajados). Solo aplica para empleados con 1 o más años de servicio.

#**Reglas:**

#- Para antigüedad igual a 1 año y menor a 3 años, el bono es del 5% de su sueldo.
#- Para antigüedad mayor o igual a 3 años y menor a 10 años, el bono es del 10% de su sueldo.
#- Para antigüedad de 10 años o más, el bono es del 20% de su sueldo.

# se necesita crear un programa que nos calcule los bonos correspondientes a cada empleado dependiendo de su tiempo en la compañia 

años_t = int(input ('digite los años laborados en la empresa'))
salario = float (input ( ' ingrese su salario actual '))

if ( años_t >= 1 and años_t < 3 ):
    bono = salario*0.05
    print ('su bono es de: ' ,bono + salario )
elif ( años_t >= 3 and años_t < 10 ):
    bono = salario*0.1
    print ('su bono es de: ' ,bono + salario )
elif ( años_t >= 10 ):
    bono = salario*0.2
    print ('su bono es de: ' ,bono + salario )
else :
    print ('aun no aplica su antiguedad para bono, su salario es de: ' ,salario )