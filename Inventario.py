"""EJERCICIO 2: SISTEMA DE INVENTARIO
===================================
Este programa gestiona un inventario simple de productos.
Permite agregar productos, ver inventario y buscar productos.

ERRORES A ENCONTRAR: 6 errores
- Errores de lógica en bucles
- Errores en condiciones
- Errores de indentación
- Errores en entrada de datos
"""
inventario = []

def cargar_inventario():

    try:
        archivo = open ("productos.txt","r")
        lineas = archivo.readlines()
        archivo.close()
        
        for linea in lineas:
            if linea.strip():
                partes = linea.strip().split(",")
                productos = {
                    "nombre": partes [0],
                    "categoria":partes[1],
                    "cantidad": int(partes[2]),
                    "precio": float(partes[3])
                }
                inventario.append(productos)
        print (f"Inventario cargado: {len(inventario)}")
    except:
        print ("Archivo de productos txt no encontrado")
    
    return inventario

def guardar_en_inventario(inventario):
    with open("productos.txt", "a", encoding="utf-8") as archivo:
        for producto in inventario:
            linea = f"{producto['nombre']},{producto['categoria']},{producto['cantidad']},{producto['precio']}\n"
            archivo.write(linea)
        print ("Producto guardado en el archivo")
    
def menu():
    print("\n=== SISTEMA DE INVENTARIO ===")
    print("1. Agregar producto")
    print("2. Ver inventario")
    print("3. Buscar producto")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def agregar_producto():
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    
    

    producto = {
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio
        
    }
    
    inventario.append(producto)
    print("Producto agregado exitosamente!")

def ver_inventario():
    if len(inventario) == 0:
        print("El inventario está vacío")
    else:
        for producto in inventario:
            total = producto["cantidad"] * producto["precio"]
            print(f"Producto: {producto['nombre']}")
            print(f"categoria: {producto['categoria']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Precio: ${producto['precio']}")
            print(f"Total: ${total}")
            print("---")

def buscar_producto():
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    encontrado = False
    
  
    for producto in inventario:
        if producto["nombre"] == nombre_buscar:
            encontrado = True
            print(f"Producto encontrado:")
            print(f"categoria: {producto['categoria']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Precio: ${producto['precio']}")
            break  
    
    if encontrado == False:
        print("Producto no encontrado")

# Programa principal
def main():
    while True:
        opcion = menu()
        
        if opcion == "1":
            agregar_producto()
            guardar_en_inventario(inventario)
            
        elif opcion == "2":
            ver_inventario()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida")

main()