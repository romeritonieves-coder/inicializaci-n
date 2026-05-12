# menu de opciones para sumar restar multiplicar y dividir 

import os

os.system('cls')

while True:
    print(' Supercalculadora ')
    print(' Que operacion deseas:\n 1. Suma\n 2. Resta\n 3. Division\n 4. Multiplicacion\n 5. Salir ')

    opcion = int(input(' Digita el numero con la operacion que deseas realizar: '))

    match opcion:
        case 1 | 2 | 3 | 4:
            num1 = float(input('Primer numero: '))
            num2 = float(input('Segundo numero: '))

            match opcion:
                case 1:
                    print(f'Resultado: {num1 + num2}')
                case 2:
                    print(f'Resultado: {num1 - num2}')
                case 3:
                    if num2 != 0:
                        print(f'Resultado: {num1 / num2}')
                    else:
                        print('Error: no se puede dividir entre cero')
                case 4:
                    print(f'Resultado: {num1 * num2}')

            input('Presione Enter para continuar')

        case 5:
            print('Gracias por su visita')
            break

        case _:
            print(' Numero invalido ')
            input('Presione Enter para seguir')