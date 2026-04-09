# Sistema de Gestión de Contactos

Proyecto del módulo 2 desarrollado en Python.

## Descripción
Esta aplicación permite registrar, editar, eliminar y buscar contactos, almacenando información personal como nombre, teléfono, correo y dirección. El sistema fue diseñado para ofrecer una gestión simple, clara y ordenada de contactos, aplicando estructuras de datos y Programación Orientada a Objetos.

## Objetivo
Desarrollar un sistema de gestión de contactos en Python que permita almacenar y administrar información personal de manera organizada, incorporando funcionalidades básicas de registro, edición, eliminación y búsqueda.

## Funcionalidades
- Agregar contactos
- Editar contactos
- Eliminar contactos
- Buscar por nombre
- Buscar por teléfono
- Listar contactos registrados

## Estructura del proyecto
- `main.py`: contiene el menú principal y la interacción con el usuario.
- `contacto.py`: define la clase `Contacto`.
- `gestor_contactos.py`: contiene la clase `GestorContactos`, encargada de administrar la lógica del sistema.
- `tests/test_gestor_contactos.py`: pruebas unitarias básicas del sistema.

## Arquitectura general
El proyecto se organiza en dos clases principales:

### Clase `Contacto`
Representa a cada contacto individual y encapsula sus datos:
- nombre
- teléfono
- correo
- dirección

También permite convertir la información del contacto en diccionario para facilitar su almacenamiento.

### Clase `GestorContactos`
Administra una lista de contactos y entrega métodos para:
- agregar contactos
- buscar contactos
- editar contactos
- eliminar contactos
- listar contactos

## Estructuras de datos utilizadas
- **Lista**: para almacenar el conjunto de contactos.
- **Diccionarios**: para representar los datos de cada contacto.
- **Clases**: para modelar el sistema con enfoque orientado a objetos.

## Requisitos
- Python 3

## Pruebas

Para ejecutar las pruebas unitarias:

python -m unittest discover tests

Resultado actual:
Ran 5 tests in 0.001s
OK

## Ejecución
Desde la terminal, ubicarse en la carpeta del proyecto y ejecutar:

```bash
python main.py
