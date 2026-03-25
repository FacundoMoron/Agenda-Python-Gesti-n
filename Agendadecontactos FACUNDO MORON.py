#---------------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      admin
#
# Created:     10/03/2026
# Copyright:   (c) admin 2026
# Licence:     <your licence>
#---------------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import os

# --- 1. CONFIGURACIÓN Y PERSISTENCIA ---
lista_contactos = []

def cargar_datos():
    """Carga los contactos del archivo al iniciar el programa."""
    if os.path.exists("agenda.txt"):
        with open("agenda.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) == 5:
                    lista_contactos.append(datos)

def guardar_datos():
    """Guarda la lista actual en el archivo de texto."""
    with open("agenda.txt", "w", encoding="utf-8") as archivo:
        for c in lista_contactos:
            archivo.write(",".join(c) + "\n")

# --- 2. FUNCIONES DE OPERACIÓN ---

def agregar_contacto():
    print("\n--- AGREGAR CONTACTO ---")
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()

    # MEJORA: Evitar duplicados por Nombre y Apellido
    for c in lista_contactos:
        if c[0].lower() == nombre.lower() and c[1].lower() == apellido.lower():
            print("⚠️ Error: El contacto ya existe.")
            return

    edad = input("Edad: ")
    # Agregamos espacio en los inputs para evitar que el texto se pegue
    tel = input("Teléfono (10 dígitos): ")
    mail = input("Email: ")

    # Validaciones técnicas requeridas
    if nombre and apellido and tel.isdigit() and len(tel) == 10:
        lista_contactos.append([nombre, apellido, tel, edad, mail])
        guardar_datos()
        print("✅ Contacto guardado correctamente.")
    else:
        print("❌ Error: Datos inválidos o incompletos.")

def ver_contactos():
    if not lista_contactos:
        print("\n⚠️ No hay contactos registrados.")
    else:
        # MEJORA: Ordenar alfabéticamente por Apellido
        lista_contactos.sort(key=lambda x: x[1].lower())
        print("\n" + "="*10 + " LISTA DE CONTACTOS " + "="*10)
        for c in lista_contactos:
            print(f"👤 {c[1]}, {c[0]} | 📱 Tel: {c[2]} | 📧 {c[4]}")

def buscar_y_retornar():
    """Función de apoyo para Buscar, Modificar y Eliminar."""
    nom = input("Nombre a buscar: ").strip().lower()
    ape = input("Apellido a buscar: ").strip().lower()
    for c in lista_contactos:
        if c[0].lower() == nom and c[1].lower() == ape:
            return c
    return None

def modificar_contacto():
    print("\n--- MODIFICAR CONTACTO ---")
    contacto = buscar_y_retornar()
    if contacto:
        print(f"\nModificando a: {contacto[0]} {contacto[1]}")
        print("1. Nombre | 2. Apellido | 3. Teléfono | 4. Mail")
        cambio = input("¿Qué desea cambiar? ")

        if cambio == "1": contacto[0] = input("Nuevo Nombre: ")
        elif cambio == "2": contacto[1] = input("Nuevo Apellido: ")
        elif cambio == "3": contacto[2] = input("Nuevo Teléfono: ")
        elif cambio == "4": contacto[4] = input("Nuevo Mail: ")

        guardar_datos()
        print("✅ Contacto actualizado.")
    else:
        print("🔍 No se encontró el contacto.")

def eliminar_contacto():
    print("\n--- ELIMINAR CONTACTO ---")
    contacto = buscar_y_retornar()
    if contacto:
        confirmar = input(f"¿Seguro que desea eliminar a {contacto[0]}? (s/n): ")
        if confirmar.lower() == 's':
            lista_contactos.remove(contacto)
            guardar_datos()
            print("🗑️ Contacto eliminado.")
    else:
        print("🔍 Contacto no encontrado.")

def exportar_planilla():
    """Genera un archivo CSV apto para Excel."""
    if not lista_contactos:
        print("\n⚠️ No hay datos para exportar.")
        return

    # Usamos punto y coma (;) para compatibilidad con Excel en Argentina
    with open("planilla_contactos.csv", "w", encoding="utf-16") as f:
        f.write("Nombre;Apellido;Telefono;Edad;Email\n")
        for c in lista_contactos:
            f.write(";".join(c) + "\n")
    print("\n📊 Planilla 'planilla_contactos.csv' generada con éxito.")

# --- 3. MENÚ PRINCIPAL ---
cargar_datos()
opcion = "0"
print("¡Bienvenidos a nuestra agenda de contactos!")

while opcion != "8":
    print("\n" + "-"*10 + " PANTALLA DE INICIO " + "-"*10)
    print("1. Mostrar saludo")
    print("2. Agregar contacto")
    print("3. Ver todos los contactos")
    print("4. Buscar contacto")
    print("5. Modificar contacto")
    print("6. Eliminar contacto")
    print("7. Exportar planilla de contactos")
    print("8. Finalizar")

    opcion = input("Elegí una opción (1-8): ")

    if opcion == "1":
        print("\n¡Hola, espero que tengas un gran día!")
    elif opcion == "2":
        agregar_contacto()
    elif opcion == "3":
        ver_contactos()
    elif opcion == "4":
        res = buscar_y_retornar()
        if res: print(f"✨ Encontrado: {res[0]} {res[1]} - Tel: {res[2]}")
        else: print("🔍 No encontrado.")
    elif opcion == "5":
        modificar_contacto()
    elif opcion == "6":
        eliminar_contacto()
    elif opcion == "7":
        exportar_planilla()
    elif opcion == "8":
        print("\n¡Gracias por utilizar nuestra agenda! Te esperamos pronto.")
    else:
        print("\n🚫 Opción inválida.")