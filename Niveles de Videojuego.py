#Un videojuego de rol (RPG) necesita determinar el **Rango del Jugador** basándose en sus Puntos de Experiencia (XP) acumulados.

#**Reglas:**

#- Si los XP son menores a 1.000, el rango es "Novato".
#- Si los XP son mayores o iguales a 1.000 y menores a 5.000, el rango es "Veterano".
#- Si los XP son mayores o iguales a 5.000 y menores a 10.000, el rango es "Maestro".
#- Si los XP son 10.000 o más, el rango es "Leyenda".

# crear un sistema de puntos para un videojuego que nod de los rangos 

puntos = int ( input ( ' ingresa tus puntos actuales en el juego '))

if ( puntos < 1000 ):
    print ( f'Su rango es "Novato" con { puntos }')
elif ( puntos >= 1000 and puntos < 5000):
    print ( f'Su rango es "Veterano" con { puntos }')
elif ( puntos >= 5000 and puntos < 10000):
    print ( f'Su rango es "Maestro" con { puntos }')
else :
    print ( f'Su rango es "Leyenda" con { puntos }')