class Contacto:
    def __init__(self, nombre, telefono, correo, direccion):
        self._nombre = nombre
        self._telefono = telefono
        self._correo = correo
        self._direccion = direccion

    def to_dict(self):
        return {
            "nombre": self._nombre,
            "telefono": self._telefono,
            "correo": self._correo,
            "direccion": self._direccion
        }