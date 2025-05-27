def calculadora():
    """
    Pide al usuario dos números y un operador, realiza la operación y muestra el resultado.
    """
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            operador = input("Ingrese el operador (+, -, *, /): ")

            if operador in ("+", "-", "*", "/"):
                if operador == "+":
                    resultado = num1 + num2
                elif operador == "-":
                    resultado = num1 - num2
                elif operador == "*":
                    resultado = num1 * num2
                else:
                    if num2 == 0:
                        print("Error: No se puede dividir por cero.")
                        continue # Volver al inicio del ciclo
                    resultado = num1 / num2
                print("El resultado es:", resultado)
            else:
                print("Error: Operador inválido.")
        except ValueError:
            print("Error: Ingrese un número válido.")
        except KeyboardInterrupt:
            print("\nPrograma terminado.")
            break # Terminar el ciclo
        finally:
            #Opcional, si se quiere preguntar si quiere hacer otra operación
            otra_operacion = input("¿Quiere realizar otra operación? (s/n): ")
            if otra_operacion.lower() != 's':
                print("No más cálculos.")
                break

if __name__ == "__main__":
    calculadora()

