# APP DE PRODUCTIVIDAD

Aplicación de POO en la creación de una app de admistración de tareas 'To Do List', permitiendo crear, modificar y visualizar listado de actividades a realizar diariamente.


### Funcionalidad de la App

Desarrollar aplicativo de productividad en Python que sirva como administrador de tareas (to do list), cumpliendo los siguientes requerimientos:

* Tener una interfaz tipo texto que facilite la interacción del usuario.
* La interfaz de usario debe poder hacer lo siguiente:
    - Visualizar estado de tareas, incluyendo la opción de filtrarlas por categoría.
    - Agregar o eliminar una tarea.
    - Modificar estado de una tarea.
    - Ver la información detallada de las taras.
* La app actualiza el listado de tareas en cada sesión almacenando la información.

### Estructura de la App

**Definición de clases (Con sus atributos y métodos)**

#### 1. **Tarea:**

*Atributos:*

- `_descripcion`: un `str` con una breve descripción de la tarea
- `_categoria`: un `str` que permitirá diferenciar un tipo de tarea de otra (ejemplo: "hogar", "trabajo", "emprendimiento", "estudio", etc.)
- `_detalle`: un `str` que podrá ser extenso y que contendrá la descripción detallada de la tarea
- `_estado`: que podrá ser `Pendiente` (valor por defecto) o `Completada`


*Métodos:*

- Un método para modificar el `_estado`
- Un método para `mostrar` en pantalla la información de la tarea.



#### 2. **Administrador:**

*Atributos:*

- `_tareas`: el listado con las tareas que vayamos agregando

*Métodos:*

- `mostrar` el listado de tareas en un formato fácil de entender por parte el usuario
- `agregar_tarea` una nueva tarea
- `actualizar_tarea` para modificar el `_estado` de una tarea
- `eliminar_tarea` para eliminar una tarea del listado
- `detalle_tarea` para imprimir en pantalla la información detallada de una tarea en particular


#### 3. **Aplicación:**

*Atributos:*

- `_administrador`: una instancia de la clase `Administrador`

*Métodos:*

- `_abrir_base_datos`: que permitirá crear/cargar la base de datos con el listado de tareas
- `_ejecutar`: que ejecutará la opción (1-6) indicada por el usuario y realizará la interacción necesaria con los objetos de las clases `Administrador` y `Tarea`
- `_actualizar_base_datos`: que permitirá actualizar la base de datos antes del cierre de la sesión

El objeto Aplicación tendrá como propósito la interacción entre el usuario y el administrador de tareas, el cual contará con una base de datos con el listado de tareas el cual se actualizará cada sesión.

Para lograr esta interacción se implementa una interfaz de texto con el siguiente menú:

- (1) Mostrar el administrador de tareas
- (2) Agregar tarea
- (3) Actualizar tarea
- (4) Eliminar tarea
- (5) Ver detalle de una tarea
- (6) Salir


