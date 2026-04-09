from contacto import Contacto
from gestor_contactos import GestorContactos

def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE CONTACTOS ---")
    print("1. Agregar contacto")
    print("2. Listar contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Eliminar contacto")
    print("6. Salir")

def main():
    gestor = GestorContactos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            direccion = input("Dirección: ")

            contacto = Contacto(nombre, telefono, correo, direccion)
            gestor.agregar_contacto(contacto)
            print("Contacto agregado correctamente.")

        elif opcion == "2":
            contactos = gestor.listar_contactos()
            if not contactos:
                print("No hay contactos registrados.")
            else:
                for c in contactos:
                    print(c)

        elif opcion == "3":
            criterio = input("Buscar por nombre o teléfono: ")
            resultados_nombre = gestor.buscar_por_nombre(criterio)
            resultado_tel = gestor.buscar_por_telefono(criterio)

            if resultados_nombre:
                for c in resultados_nombre:
                    print(c)
            elif resultado_tel:
                print(resultado_tel)
            else:
                print("No se encontraron contactos.")

        elif opcion == "4":
            telefono_actual = input("Ingrese el teléfono actual del contacto a editar: ")
            nuevo_nombre = input("Nuevo nombre (Enter para omitir): ")
            nuevo_telefono = input("Nuevo teléfono (Enter para omitir): ")
            nuevo_correo = input("Nuevo correo (Enter para omitir): ")
            nueva_direccion = input("Nueva dirección (Enter para omitir): ")

            resultado = gestor.editar_contacto(
                telefono_actual,
                nuevo_nombre if nuevo_nombre else None,
                nuevo_telefono if nuevo_telefono else None,
                nuevo_correo if nuevo_correo else None,
            nueva_direccion if nueva_direccion else None
            )

            if resultado == "ok":
                print("Contacto editado correctamente.")
            elif resultado == "telefono_duplicado":
                print("No se puede cambiar el teléfono: ya existe otro contacto con ese número.")
            else:
                print("No se encontró el contacto.")

        elif opcion == "5":
            telefono = input("Ingrese el teléfono del contacto a eliminar: ")
            eliminado = gestor.eliminar_contacto(telefono)

            if eliminado:
                print("Contacto eliminado correctamente.")
            else:
                print("No se encontró el contacto.")

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()