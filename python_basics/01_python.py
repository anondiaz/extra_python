entero = 1
decimal = 1.2
cadena1 = "Soy un texto"
cadena2 = 'Soy otro texto'
verdadero = True
falso = False
PI = 3.14159
PI = 6

uno, dos, tres = 1, 2, 3

'''
Soy un comentario
de varias lineas
y no afecta al programa
'''
#Yo tambien soy un comentario

# print(cadena1)

# nombre = input("Dime tu nombre: ") # input() es una función que recibe un texto y devuelve un string
# print(type(nombre))
# print(f"Hola {nombre}")

# edad = input("Dime tu edad: ")
# edad = int(edad)  # Convertimos la edad a un entero
# if edad < 10:
#     print("Eres un niño")
# elif edad < 18:
#     print("Eres menor de edad")
# else:
#     print("Eres mayor de edad")

nums = [1, 2, 3, 4, 5] # Esto es una lista ~ array en otros lenguajes
for num in nums:
    print(num)

diccionario = {
    "nombre": "Peter",
    "apellido": "Demostenes"}
diccionario["nombre"] = "Juan"
print(diccionario)

i = 1
while i < 5:
    print(i)
    i += 1

j = 1
while True:
    print(j)
    j += 1
    if j == 5:
        break  # Rompe el bucle cuando j es igual a 5

def saludo(nombre):
    """
    Esta función recibe un nombre y devuelve un saludo.
    :param nombre: str
    :return: str
    """
    print (f"Hola {nombre}")
saludo("Matins")

def suma(num1, num2):
    return num1 + num2
resultado = suma(2, 3)
print(f"La suma es: {resultado}")