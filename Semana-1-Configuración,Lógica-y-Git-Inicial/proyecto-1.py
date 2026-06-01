from os import O_APPEND
x = 1

numero_1 = int(input(f"Ingrese el {x}° numero: "))
numero_2 = int(input(f"Ingrese el {x+1}° numero: "))

suma = numero_1 + numero_2
print(f"La suma de los numeros es: {suma}")

#Guardar en un archivo de texto
archivo = open("resultado.txt", "w")
