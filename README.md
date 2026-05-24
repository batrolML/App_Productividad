# APP DE PRODUCTIVIDAD

Aplicación de POO en la creación de una app de adimistración de tareas 'To Do List', permitiendo crear, modificar y visualizar listado de actividades a realizar diariamente.


### Funcionalidad de la App

Desarrollar aplicativo de productividad en Python que sirva como administrador de tareas (to do list), cumpliendo los siguientes requerimientos:

* Tener una interfaz tipo texto que facilite la interacción del usuario.
* La interfaz de usario debe ser poder hacer lo siguiente:
    - Visualizar estado de tareas, incluyendo la opción de filtrarlas por categoría.
    - Agregar o eliminar una tarea.
    - Modificar estado de una tarea.
    - Ver la información detallada de las taras.
* La app actualiza el listado de tareas en cada sesión almacenando la información.

### Estructura de la App

**Definición de clases (Con sus atributos y métodos)**

1. **Tarea:**

    Atributos:

- `_descripcion`: un `str` con una breve descripción de la tarea
- `_categoria`: un `str` que permitirá diferenciar un tipo de tarea de otra (ejemplo: "hogar", "trabajo", "emprendimiento", "estudio", etc.)
- `_detalle`: un `str` que podrá ser extenso y que contendrá la descripción detallada de la tarea
- `_estado`: que podrá ser `Pendiente` (valor por defecto) o `Completada`


    Métodos:
- Un método para modificar el `_estado`
- Un método para `mostrar` en pantalla la información de la tarea


2. *Administrador.* Contendrá lo siguiente:
    - Datos = Listado de tareas.
    - Acciones = Mostrar el listado | agregar/modificar/eliminar | Ver detalle de la tarea. 

3. *Aplicación.* Contendrá lo siguiente:
    - Datos = Interacción del usuario (datos ingresados por usuario)
    - Acciones = Interacción con el administrador y las tareas así como el almacenamiento de modificaciones hechas en sus respectivas sesiones previas.



