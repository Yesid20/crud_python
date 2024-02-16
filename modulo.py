import json

def registro():
    # Cargar archivo json para lectura 
    with open('registro.json', 'r') as archivo:
        data_existing = json.load(archivo)

    new_person = int(input("Ingresa numero de cedula: "))
    new_per = {
        "id": new_person,
        "nombre": input("Ingrese su nombre: "),
        "apellido": input("Ingrese su apellido: "),
        "edad": int(input("Ingrese su edad: ")),
        "profesion": input("Ingrese su profesion: ")
    }

    data_existing.append(new_per)

    # Guardar los datos en el archivo JSON
    with open('registro.json', 'w') as archivo:
        json.dump(data_existing, archivo)

def leer():
    ##cargar json
    with open('registro.json', 'r') as archivo:
        data = json.load(archivo)

    # Imprimir solo los campos id y nombre
        for registro in data:
            print("ID:", registro.get("id", "N/A"), "| Nombre:", registro.get("nombre", "N/A"))

def actualizar():
    with open('registro.json', 'r') as archivo:
        data = json.load(archivo)

        id_buscar = int(input("id a buscar: "))

        for registro in data:
            if registro.get("id") == id_buscar:
                nuevo_name = input("ingresa el nuevo nombre; ")
                registro["nombre"] = nuevo_name

    with open('registro.json', 'w') as archivo:
        json.dump(data, archivo)

import json

def eliminar_registro():
        # Abrir archivo JSON para lectura
        with open('registro.json', 'r') as archivo:
            data = json.load(archivo)
        
        # Solicitar al usuario el ID a eliminar
        id_eliminar = int(input("Ingrese el ID a eliminar: "))
        
        # Eliminar el registro por su ID
        data = [registro for registro in data if registro.get("id") != id_eliminar]
        
        # Guardar los datos actualizados en el archivo JSON
        with open('registro.json', 'w') as archivo:
            json.dump(data, archivo)
            
   

