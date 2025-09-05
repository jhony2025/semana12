Gestión de Inventario de Biblioteca
Descripción

Este proyecto implementa un sistema de gestión de inventario de biblioteca en Python, que permite registrar, actualizar y consultar libros disponibles, así como controlar préstamos y devoluciones. Es ideal para pequeñas bibliotecas o proyectos educativos que necesitan mantener un inventario organizado de manera sencilla.

Funciones principales:

Registrar nuevos libros con información básica (título, autor, año, cantidad disponible).

Consultar la lista de libros disponibles.

Actualizar la información de un libro.

Controlar préstamos y devoluciones.

Eliminar libros del inventario de manera segura.

Tecnologías utilizadas

Python 3.x

Librerías estándar (os, json)

Instalación

Clonar el repositorio:

git clone https://github.com/tu-usuario/gestion-inventario-biblioteca.git


Acceder al directorio del proyecto:

cd gestion-inventario-biblioteca


Instalar dependencias (opcional):

pip install -r requirements.txt


Nota: El proyecto utiliza principalmente librerías estándar de Python, por lo que puede ejecutarse sin instalaciones adicionales.

 Uso

Importar el módulo principal:

from biblioteca import Inventario


Crear una instancia del inventario:

inventario = Inventario()


Operaciones disponibles:

Agregar libro
inventario.agregar_libro("El Principito", "Antoine de Saint-Exupéry", 1943, 5)

Consultar libros
inventario.mostrar_libros()

Actualizar libro
inventario.actualizar_libro("El Principito", cantidad=10)

Registrar préstamo
inventario.prestar_libro("El Principito")

Registrar devolución
inventario.devolver_libro("El Principito")

Eliminar libro
inventario.eliminar_libro("El Principito")

Ejemplo completo
from biblioteca import Inventario

inventario = Inventario()

# Agregar libros
inventario.agregar_libro("El Principito", "Antoine de Saint-Exupéry", 1943, 5)
inventario.agregar_libro("1984", "George Orwell", 1949, 3)

# Mostrar libros disponibles
inventario.mostrar_libros()

# Registrar un préstamo
inventario.prestar_libro("1984")

# Actualizar cantidad de un libro
inventario.actualizar_libro("El Principito", cantidad=10)

# Registrar devolución
inventario.devolver_libro("1984")

# Eliminar un libro
inventario.eliminar_libro("El Principito")

# Mostrar estado final
inventario.mostrar_libros()

 Contribuciones

Las contribuciones son bienvenidas. Puedes abrir un pull request o issue para sugerir mejoras o reportar errores.

Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE
 para más detalles.
