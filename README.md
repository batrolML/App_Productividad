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

**Definición de clases (Atributos y Métodos)**

1. *Tarea.* Contedrá lo siguiente:
    - Datos = Descripción | Categoría | Detalles | Estado
    - Acciones = Modificar estado | Visualizar detalles de tarea 


2. *Administrador.* Contendrá lo siguiente:
    - Datos = Listado de tareas.
    - Acciones = Mostrar el listado | agregar/modificar/eliminar | Ver detalle de la tarea. 

3. *Aplicación.* Contendrá lo siguiente:
    - Datos = Interacción del usuario (datos ingresados por usuario)
    - Acciones = Interacción con el administrador y las tareas así como el almacenamiento de modificaciones hechas en sus respectivas sesiones previas.



