class GestorContactos:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto.to_dict())

    def listar_contactos(self):
        return self.contactos

    def buscar_por_nombre(self, nombre):
        resultados = []
        for contacto in self.contactos:
            if nombre.lower() in contacto["nombre"].lower():
                resultados.append(contacto)
        return resultados

    def buscar_por_telefono(self, telefono):
        for contacto in self.contactos:
            if contacto["telefono"] == telefono:
                return contacto
        return None

    def eliminar_contacto(self, telefono):
        for i, contacto in enumerate(self.contactos):
            if contacto["telefono"] == telefono:
                del self.contactos[i]
                return True
        return False

    def editar_contacto(
        self,
        telefono_actual,
        nuevo_nombre=None,
        nuevo_telefono=None,
        nuevo_correo=None,
        nueva_direccion=None
    ):
        contacto = self.buscar_por_telefono(telefono_actual)

        if contacto is None:
            return "no_encontrado"

        if nuevo_telefono:
            existente = self.buscar_por_telefono(nuevo_telefono)
            if existente is not None and existente is not contacto:
                return "telefono_duplicado"

        if nuevo_nombre:
            contacto["nombre"] = nuevo_nombre
        if nuevo_telefono:
            contacto["telefono"] = nuevo_telefono
        if nuevo_correo:
            contacto["correo"] = nuevo_correo
        if nueva_direccion:
            contacto["direccion"] = nueva_direccion

        return "ok"