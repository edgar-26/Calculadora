
import Operaciones

print("=== CALCULADORA BASICA ===")

# Solicitar dos numeros
a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))

# Mostrar las operaciones disponibles
print("\nSeleccione una operacion:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")

opcion = input("Ingrese una opcion (1-4): ")

# Realizar la operacion seleccionada
if opcion == "1":
    resultado = Operaciones.sumar(a, b)

elif opcion == "2":
    resultado = Operaciones.restar(a, b)

elif opcion == "3":
    resultado = Operaciones.multiplicar(a, b)

elif opcion == "4":
    resultado = Operaciones.dividir(a, b)

else:
    resultado = "Error: Opcion no valida."

# Mostrar resultado
print("\nResultado:", resultado)