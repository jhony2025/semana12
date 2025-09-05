# ============================
# Sistema de Biblioteca Digital
# ============================

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Título y autor en tupla inmutable
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} de {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # ISBN : Libro
        self.usuarios = {}  # ID : Usuario
        self.ids_usuarios = set()  # Conjunto para IDs únicos

    # -------------------
    # Gestión de Libros
    # -------------------
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"✅ Libro '{libro.info[0]}' agregado con éxito.")
        else:
            print("⚠️ El libro ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            print(f"❌ Libro '{eliminado.info[0]}' eliminado.")
        else:
            print("⚠️ El libro no existe en la biblioteca.")

    # -------------------
    # Gestión de Usuarios
    # -------------------
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"✅ Usuario '{usuario.nombre}' registrado.")
        else:
            print("⚠️ El ID de usuario ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            eliminado = self.usuarios.pop(id_usuario)
            self.ids_usuarios.remove(id_usuario)
            print(f"❌ Usuario '{eliminado.nombre}' dado de baja.")
        else:
            print("⚠️ El usuario no existe.")

    # -------------------
    # Préstamos
    # -------------------
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("⚠️ Usuario no encontrado.")
            return
        if isbn not in self.libros:
            print("⚠️ Libro no disponible en la biblioteca.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros.pop(isbn)  # Se retira de disponibles
        usuario.libros_prestados.append(libro)
        print(f"📚 Libro '{libro.info[0]}' prestado a {usuario.nombre}.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("⚠️ Usuario no encontrado.")
            return

        usuario = self.usuarios[id_usuario]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros[isbn] = libro
                print(f"🔄 Libro '{libro.info[0]}' devuelto por {usuario.nombre}.")
                return
        print("⚠️ El usuario no tiene este libro prestado.")

    # -------------------
    # Búsqueda de Libros
    # -------------------
    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.info[0].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.info[1].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)

        if resultados:
            print("🔎 Resultados de búsqueda:")
            for l in resultados:
                print(" -", l)
        else:
            print("⚠️ No se encontraron libros con ese criterio.")

    # -------------------
    # Listar libros prestados
    # -------------------
    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios:
            print("⚠️ Usuario no encontrado.")
            return

        usuario = self.usuarios[id_usuario]
        if usuario.libros_prestados:
            print(f"📖 Libros prestados a {usuario.nombre}:")
            for l in usuario.libros_prestados:
                print(" -", l)
        else:
            print(f"ℹ️ {usuario.nombre} no tiene libros prestados.")
