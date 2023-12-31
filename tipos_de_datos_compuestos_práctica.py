"""Tipos_de_datos_compuestos_Práctica.ipynb


---
# ***Argentina Programa 4.0 - Programación Avanzada con Python***
---

## **Módulo 3**: Tipos de Datos Compuestos - Práctica

### ***Universidad Nacional de Chilecito***

---

# Cadena de Caracteres

* Dada una cadena, escriba un programa que cuente cuántas veces aparece una letra específica en la cadena.
"""

cadena = input("Ingrese una cadena: ")
letra = input("Ingrese la letra que desea contar: ")
print(cadena.count(letra))



"""* Escriba un programa que invierta una cadena. Por ejemplo, "hola" se convierte en "aloh"."""

cadena = input("Ingrese una cadena: ")
print(cadena[::-1])





"""
* Dada una cadena, escriba un programa que elimine todos los caracteres duplicados y muestre la cadena resultante."""

cadena = "aabbcdeeffgh"

for i in cadena:

  if cadena.count(i)>1:
    cadena = cadena.replace(i,"",1)

print(cadena)



"""# Listas

* Dada una lista de números, escriba un programa que encuentre el número más grande.
"""

numeros = [2, 5, 3, 8, 1, 10, 6]
print(max(numeros))



"""* Escriba un programa que ordene una lista de números en orden ascendente o descendente."""

numeros = [2, 5, 3, 8, 1, 10, 6]

# Ascendente
numeros.sort()
print(numeros)

# Descendente
numeros.sort(reverse=True)
print(numeros)

"""* Dada una lista de cadenas, escriba un programa que encuentre la cadena más larga."""

cadenas = ["Hola", "Mundo", "Python", "Lenguaje", "Programación"]

x = cadenas[0]
for i in cadenas:
  if len(i)>len(x):
    x = i

print(x)



"""# Diccionarios

* Dada una lista de nombres de frutas y sus colores, escriba un programa que cree un diccionario con las frutas como claves y los colores como valores.
"""

frutas = [("Manzana", "Rojo"), ("Banana", "Amarillo"), ("Naranja", "Naranja"), ("Pera", "Verde")]

for i,j in frutas:
  frutas_colores[i] = j
print(frutas_colores)

"""* Dado un diccionario que asocia nombres de frutas con sus calorías, escriba un programa que encuentre la fruta con el menor número de calorías."""

frutas_calorias = {"Manzana": 52, "Banana": 89, "Naranja": 47, "Pera": 57}

min(frutas_calorias, key=frutas_calorias.get)



"""* Escriba un programa que encuentre todas las claves en un diccionario que corresponden a un valor específico."""

diccionario = {"Manzana": "Rojo", "Banana": "Amarillo", "Naranja": "Naranja", "Pera": "Verde", "Limon": "Amarillo"}

valor_buscado = "Amarillo"

lista = list(diccionario.items())
dicci ={}
for i,j in lista:
  if j == valor_buscado:
    dicci[i] =j

    print(i)
dicci.keys()



"""# Problema

Se tiene una lista de nombres de personas con sus respectivas edades, pero algunos de los nombres están mal escritos o en mayúsculas y otros en minúsculas. Además, se tiene un diccionario que asocia nombres y apellidos con sus apodos. Escriba un programa que corrija los nombres mal escritos y agregue los apodos a cada nombre, y luego cree una lista de todas las personas mayores de 18 años y las ordene alfabéticamente por sus nombres completos.
"""

# Lista de personas con sus edades
personas = [
    "Juan Perez, 24",
    "Maria Gonzalez, 18",
    "PEDRO RODRIGUEZ, 32",
    "ana Maria Garcia, 21",
    "Luis ramirez, 16",
    "josefa hernandez, 28"
]

# Diccionario de apodos
apodos = {
    "Juan Perez": "Juancho",
    "Maria Gonzalez": "Mari",
    "Pedro Rodriguez": "Peter",
    "Ana Maria Garcia": "Anita",
    "Luis Ramirez": "Lucho",
    "Josefa Hernandez": "Chefa"
}

#Lista apodos
solo_apodos = list(apodos.values())


#Lista nombres y edades
nombres = []
edades = []
for i in personas:
  nombres.append(i[0:i.find(" ")].title())
  edades.append(int(i[i.find(","):].replace(",","").strip()))


#Diccionario nombres y apodos
diccio = {}
n = 0
for i in nombres:
  diccio[i] = solo_apodos[n]
  n += 1


#Nombres Completos y edades
n2 = 0
nombre_edades = {}

for i in apodos:
  if edades[n2]>18:
    nombre_edades[i] = edades[n2]
  n2 += 1

#Muestra en pantalla
sorted(nombre_edades.items())

print(diccio)
print(sorted(nombre_edades.items()))

