# test_biblioteca.py
from biblioteca import Libro, Usuario, Biblioteca

def main():
    print("\n=== PRUEBAS DEL SISTEMA DE BIBLIOTECA ===\n")

    # Crear biblioteca
    biblio = Biblioteca()

    # Crear libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "1111")
    libro2 = Libro("El Quijote", "Miguel de Cervantes", "Clásico", "2222")
    libro3 = Libro("Python para Todos", "Charles Severance", "Tecnología", "3333")

    # Agregar libros
    biblio.agregar_libro(libro1)
    biblio.agregar_libro(libro2)
    biblio.agregar_libro(libro3)

    # Registrar usuarios
    usuario1 = Usuario("Ana Pérez", "U001")
    usuario2 = Usuario("Luis Gómez", "U002")
    biblio.registrar_usuario(usuario1)
    biblio.registrar_usuario(usuario2)

    # Préstamos
    print("\n--- Préstamo de libro ---")
    biblio.prestar_libro("U001", "1111")
    biblio.listar_libros_prestados("U001")

    # Intentar prestar un libro que no está disponible
    biblio.prestar_libro("U002", "1111")

    # Devolución
    print("\n--- Devolución de libro ---")
    biblio.devolver_libro("U001", "1111")
    biblio.listar_libros_prestados("U001")

    # Búsquedas
    print("\n--- Búsqueda de libros ---")
    biblio.buscar_libros("titulo", "Quijote")
    biblio.buscar_libros("autor", "García Márquez")
    biblio.buscar_libros("categoria", "Tecnología")

    # Baja de usuario
    print("\n--- Baja de usuario ---")
    biblio.dar_baja_usuario("U002")

    # Eliminar libro
    print("\n--- Eliminar libro ---")
    biblio.quitar_libro("3333")

if __name__ == "__main__":
    main()
