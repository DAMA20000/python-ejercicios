diccionario = {
    "nombre": "Damaris",
    "edad": 25,
    "ciudad": "San salvador de jujuy"
}
print(diccionario)
print("Nombre:", diccionario["nombre"])
print("Edad:", diccionario["edad"])
print("Ciudad:", diccionario["ciudad"])



diccionario['Ladra'] = "Si"
print(diccionario)
diccionario.pop('Ladra')
print(diccionario)
# diccionario.pop('Ladra') elimina la clave 'Ladra' del diccionario y su valor asociado. Si intentas eliminar una clave que no existe, se generará un error. Por eso es importante asegurarse de que la clave exista antes de intentar eliminarla.
#diccionario.popitem() elimina el último elemento agregado al diccionario. Si el diccionario está vacío, se generará un error. Es útil para eliminar elementos de un diccionario sin necesidad de conocer la clave específica.
copiaGato = diccionario.copy()
print(copiaGato)

print(diccionario, copiaGato)
# del diccionario['Ladra'] elimina la clave 'Ladra' del diccionario. Si intentas eliminar una clave que no existe, se generará un error. Es importante asegurarse de que la clave exista antes de intentar eliminarla para evitar errores en el programa.

diccionario.clear()
print(diccionario)

diccionario.update({"nombre": "Damaris", "edad": 25, "ciudad": "San salvador de jujuy"})
print(diccionario)  

#Dataset simple de una persona(estructura de datos)
# Este ejercicio simula un registro de datos, algo muy comun en analisis de datos, donde cada persona tiene un nombre, edad y ciudad. El diccionario es una estructura de datos que permite almacenar esta información de manera organizada y fácil de acceder. Al usar diccionarios, podemos asociar cada valor con una clave descriptiva, lo que facilita la lectura y manipulación de los datos.
persona = {
    "nombre": "Damaris",
    "edad": 25,
    "ciudad": "San Salvador de Jujuy",
    "profesion": "Data Scientist"
}

print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])
print("Ciudad:", persona["ciudad"])
print("Profesión:", persona["profesion"])

# Concepto de Data Science
# Esto es equivalente a una fila en una base de datos o dataset

#Diccionarios con listas como valores(Mini dataset)

# Ahora simulamos datos de ventas.

ventas = {
    "producto": "Torta",
    "precios": [1200, 1500, 1800, 2000]
}

promedio = sum(ventas["precios"]) / len(ventas["precios"])

print("Producto:", ventas["producto"])
print("Precios:", ventas["precios"])
print("Precio promedio:", promedio)