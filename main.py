print("Hola, bienvenido a la calculadora")
print("¿Qué operación deseas realizar?")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
operacion=input("Ingresa el número de la operación: ")
a=input("Ingresa el primer número: ")
b=input("Ingresa el segundo número: ")
if operacion=="1":
    print("La suma es: ",calcular_suma(float(a),float(b)))
elif operacion=="2":
    print("La resta es: ",calcular_resta(float(a),float(b)))
elif operacion=="3":
    print("La multiplicación es: ",multiplica(float(a),float(b)))
elif operacion=="4":
    print("La división es: ",divide(float(a),float(b)))

print('¡Gracias por usar la calculadora!')