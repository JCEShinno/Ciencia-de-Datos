import unittest
from contacto import Contacto
from gestor_contactos import GestorContactos

class TestGestorContactos(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorContactos()
        self.contacto = Contacto("Juan", "123", "juan@mail.com", "Santiago")
        self.gestor.agregar_contacto(self.contacto)

    def test_agregar_contacto(self):
        self.assertEqual(len(self.gestor.contactos), 1)

    def test_buscar_por_telefono(self):
        resultado = self.gestor.buscar_por_telefono("123")
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado["nombre"], "Juan")

    def test_eliminar_contacto(self):
        eliminado = self.gestor.eliminar_contacto("123")
        self.assertTrue(eliminado)
        self.assertEqual(len(self.gestor.contactos), 0)
    
    def test_editar_telefono_correctamente(self):
        resultado = self.gestor.editar_contacto("123", nuevo_telefono="999")
        self.assertEqual(resultado, "ok")

        contacto = self.gestor.buscar_por_telefono("999")
        self.assertIsNotNone(contacto)
        self.assertEqual(contacto["nombre"], "Juan")

    def test_no_permitir_telefono_duplicado(self):
        contacto2 = Contacto("Ana", "456", "ana@mail.com", "Valparaíso")
        self.gestor.agregar_contacto(contacto2)

        resultado = self.gestor.editar_contacto("123", nuevo_telefono="456")
        self.assertEqual(resultado, "telefono_duplicado")

if __name__ == "__main__":
    unittest.main()