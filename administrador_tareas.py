# Importar librería
import textwrap, os, csv


# Clase Tarea
class Tarea:
    # Inicialización (Argumentos de entrada)
    def __init__(self, descripcion, categoria, detalles):

        # Definición de atributos
        self._descripcion = descripcion
        self._categoria = categoria
        self._detalles = detalles
        self._estado = "Pendiente"  # Valor por defecto será pendiente

    # Otorgar acceso a usuario para visualizar atributos
    @property
    def descripcion(self):
        """Retorna descripción de tarea"""
        return self._descripcion

    @property
    def categoria(self):
        """retorna categoría de tarea"""
        return self._categoria

    @property
    def detalles(self):
        """Retorna detalle de tarea"""
        return self._detalles

    @property
    def estado(self):
        """Retorna el estado de la tarea"""
        return self._estado

    # Otorgar acceso a usuario para modificar atributo `estado`
    @estado.setter
    def estado(self, nuevo_estado):
        """Modificar estado de tarea"""
        self._estado = nuevo_estado

    # Métodos
    def mostrar(self):
        """Imprime información detallada de una tarea"""

        # Configuración para que la información aparezca en multiples líneas de texto
        ancho = 80

        str_detalles = f"Detalles: {self._detalles}"
        if len(str_detalles) > ancho:
            detalles = textwrap.fill(str_detalles, width=ancho)
        else:
            detalles = str_detalles

        print("--" * ancho)
        print(f"Tarea: {self._descripcion}")
        print("--" * ancho)
        print(f"Categoría: {self._categoria}")
        print(".." * ancho)
        print(f"estado: {self._estado}")
        print(".." * ancho)
        print(detalles)
        print("--" * ancho)


# Clase Administrador
class Administrador:
    # Inicialización
    def __init__(self):
        self._tareas = []

    # Decorador para otorgar acceso a visualziar las tareas (atributo privado self._tareas)
    @property
    def tareas(self):
        return self._tareas

    # Métodos
    def mostrar(self, categoria=None):
        """Imprime en formato tabla el ID, Descripción, categoría y estado de cada tarea en el listado"""

        # Estructura para impresiones
        if len(self._tareas) != 0:
            ancho_col = 80

            # Imprimir encabezado
            formato_cols = "{0:<6} {1:<35} {2:<25} {3:<11}"
            print("--" * ancho_col)
            print(formato_cols.format("ID", "Tarea", "Categoría", "Estado"))
            print("--" * ancho_col)

            # Impresión de tareas
            if (
                categoria == None
            ):  # si está vacío imprime todas las categorías existentes
                for ID, tarea in enumerate(self._tareas):
                    print(
                        formato_cols.format(
                            str(ID + 1),
                            tarea.descripcion,
                            tarea.categoria,
                            tarea.estado,
                        )
                    )
                    print(".." * ancho_col)
            else:  # Imprime tareas por categoría
                for ID, tarea in enumerate(self._tareas):
                    if tarea.categoria == categoria:
                        print(
                            formato_cols.format(
                                str(ID + 1),
                                tarea.descripcion,
                                tarea.categoria,
                                tarea.estado,
                            )
                        )
                        print(".." * ancho_col)
        else:
            print("*** NO HAY TAREAS DISPONIBLES ***")

    def agregar_tarea(self, tarea):
        """Agregar tarea a la lista de tareas"""
        self._tareas.append(tarea)

    def actualizar_tarea(self, ID):
        """Modificar estado de tarea"""
        if len(self._tareas) != 0:
            try:
                if self._tareas[ID - 1].estado == "Pendiente":
                    # Cambiar estado a completada
                    self._tareas[ID - 1].estado = "Completada"
                else:
                    # Cambiar a estado pendiente
                    self._tareas[ID - 1].estado = "Pendiente"
            except:
                print("*** NO EXISTE ID ***")
        else:
            print("*** NO HAY TAREAS DISPONIBLES ***")

    def eliminar_tarea(self, ID):
        """Eliminar tarea de lista"""
        if len(self._tareas) != 0:
            try:
                self._tareas.pop(ID - 1)
            except:
                print("*** NO EXISTE ID ***")
        else:
            print("*** NO HAY TAREAS DISPONIBLES ***")

    def detalle_tarea(self, ID):
        if len(self.tareas) != 0:
            try:
                self._tareas[ID - 1].mostrar()
            except:
                print("*** NO EXISTE ID ***")
        else:
            print("*** NO HAY TAREAS DISPONIBLES ***")


# Clase Aplicacion
class App:
    def __init__(self):
        self._administrador = Administrador()

        # Para abrir o crear base de datos
        self._abrir_base_datos()

    def _abrir_base_datos(self):
        # verifica existencia de archivo csv - Almacena el listado de tareas - Crea archivo vacío
        if os.path.isfile("./tareas.csv"):
            self._agregar_tareas()
            self._administrador.mostrar()
        else:
            with open("./tareas.csv", "w"):
                pass
        # Ejecutar app después de verificación
        self._ejecutar()

    def _agregar_tareas(self):
        with open("./tareas.csv", "r") as archivo:
            reader = csv.reader(archivo)

            for fila in reader:
                tarea = Tarea(fila[0], fila[1], fila[2])
                if fila[3] == "Completada":
                    tarea.estado = "Completada"
                self._administrador.agregar_tarea(tarea)

    def _ejecutar(self):

        continuar = True  # Blucle

        while continuar:
            print("\n\nSeleccione una opción: ")
            print("  (1) Mostrar Administrador de Tareas")
            print("  (2) Agregar Tarea")
            print("  (3) Actualizar Tarea")
            print("  (4) Eliminar Tarea")
            print("  (5) Ver Detalle")
            print("  (6) Salir")

            opcion = int(input("Opción: "))

            if opcion == 1:  # Activa opción de mostrar administrador de tareas
                print("\n Indique las categorías a mostrar: (a) todas, (b) filtrar")
                opcion_cat = input("   Opción:   ")

                if opcion_cat.lower() == "a":
                    self._administrador.mostrar()
                else:
                    print("\n   Especifíque la categoría a mostrar:   ")
                    cat = input("   Categoría:   ")
                    self._administrador.mostrar(categoria=cat)
            elif opcion == 2:  # Activa la opción de agregar tarea
                print("Información de la tarea a agregar:  ")
                descripcion = input("Descripción: ")
                categoria = input("Categoría: ")
                detalles = input("Detalles: ")
                tarea = Tarea(descripcion, categoria, detalles)
                self._administrador.agregar_tarea(tarea)
                self._administrador.mostrar()
            elif opcion == 3:  # Activa la opción de actualizar tarea
                self._administrador.mostrar()
                print("\nID de la tarea a actualizar: ")
                ID = int(input("ID: "))
                self._administrador.actualizar_tarea(ID)
                self._administrador.mostrar()
            elif opcion == 4:  # Activa la opción de eliminar tarea
                self._administrador.mostrar()
                print("\nID de tarea a eliminar: ")
                ID = int(input("ID: "))
                respuesta = input("¿Está seguro de eliminar la tarea? (S/N): ")
                if respuesta.lower() == "s":
                    self._administrador.eliminar_tarea(ID)
                self._administrador.mostrar()
            elif opcion == 5:  # Activa la opción de ver detalle
                self._administrador.mostrar()
                print("\nIntroduzca el ID de la tarea que quiere ver a detalle: ")
                ID = int(input("ID: "))
                self._administrador.detalle_tarea(ID)
            elif opcion == 6:  # Activa la opción para salir
                continuar = False
                self._actualizar_base_datos()
                break
            else:
                print("Debe seleccionar una opción entre 1 y 6")
            input("Oprima una tecla para continuar")

            # Limpiar pantalla
            os.system("clear")  # Sirve en linux

    def _actualizar_base_datos(self):
        with open("./tareas.csv", "w") as archivo:
            writer = csv.writer(archivo)

            if len(self._administrador.tareas) != 0:
                for tarea in self._administrador._tareas:
                    fila = [
                        tarea.descripcion,
                        tarea.categoria,
                        tarea.detalles,
                        tarea.estado,
                    ]
                    writer.writerow(fila)


# Función main para ejecutar desde terminal
if __name__ == "__main__":
    app = App()
