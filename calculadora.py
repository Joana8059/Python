#CalculadoraSimple
num1 = float(input("Ingrese"))
num2 = float (input (´Ingrese el segundo número: ´))

operacion = input (´Ingrese la operación(+,-,*,/): ´)

if operacion == ´+´:
    resultado = num1 + num2
    print (´Resultado:´ resultado)

elif operacion == ´-´:
    resultado = num1 - num2
    print(´Resultado: ´ resultado)

elif operacion == ´*´:
    resultado = num1 * num2
    print(´Resultado: ´ resultado)

elif operacion == ´/´: 
    if num2 == 0:
        print(´ Error: No se puede dividir por cero´)
    else:
    resultado = num1 / num2
    print(´Resultado: ´ resultado)

else:
    print(´Error: Operación no válida.´)