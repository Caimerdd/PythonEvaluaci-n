class Alumno:
    def __init__(self, nombre, edad, carrera, calificaciones=None ):  
        if calificaciones is None:
            calificaciones = []
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = calificaciones
         
    
    def promedio(self):
        if len(self.calificaciones) > 0:
            return sum(self.calificaciones) / len(self.calificaciones)
            return 0.0
        else:
            return print("No hay calificaciones para calcular el promedio.")
        
    def mostrar_informacion(self,numero=None):
        encabezado = f"\nEstudiante #{numero}" if numero else "\nEstudiante:"
        print(encabezado)
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")
        print(f"Calificaciones: {', '.join(map(str, self.calificaciones))}")
        print(f"Promedio: {self.promedio():.2f}")
        
estudiantes = {}
contador_estudiantes = 0

def registrar_estudiante():
    global contador_estudiantes
    nombre = input("Nombre del estudiante: ").strip()
    try:
        edad = int(input("Edad del estudiante: "))
        carrera = input("Carrera del estudiante: ").strip()
        estudiante = Alumno(nombre, edad, carrera)
        contador_estudiantes += 1
        estudiantes[contador_estudiantes] = estudiante
        print(f"Estudiante registrado con éxito como ID #{contador_estudiantes}.")
    except ValueError:
        print("Error: la edad debe ser un número entero.")
        
def agregar_calificacion_estudiante():
    try:
        id_est = int(input("Ingrese el número del estudiante (ID): "))
        estudiante = estudiantes.get(id_est)
        if estudiante:
            while True:
                nota = float(input("Ingrese la calificación a agregar: "))
                if 0 <= nota <= 100:
                    estudiante.agregar_calificacion(nota)
                else:
                    print("La calificación debe estar entre 0 y 100.")
                    continue
                otra = input("¿Desea agregar otra calificación? (s/n): ").strip().lower()
                if otra != 's':
                    break
        else:
            print("No se encontró un estudiante con ese ID.")
    except ValueError:
        print("Error: debes ingresar un número válido.")

def mostrar_info_estudiante():
    try:
        id_est = int(input("Ingrese el número del estudiante (ID): "))
        estudiante = estudiantes.get(id_est)
        if estudiante:
            estudiante.mostrar_informacion(numero=id_est) 
        else:
            print("No se encontró un estudiante con ese ID.")
    except ValueError:
        print("Error: debes ingresar un número válido.")

def mostrar_todos_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    for id_est, estudiante in estudiantes.items():
        estudiante.mostrar_informacion(numero=id_est)

def alumno_agregar_calificacion(self, nota: float):
    if 0 <= nota <= 100:
        self.calificaciones.append(nota)
        print("Calificación agregada correctamente.")
    else:
        print("La calificación debe estar entre 0 y 100.")

Alumno.agregar_calificacion = alumno_agregar_calificacion


def menu():
    while True:
        print(" ")
        print("1. Registrar nuevo estudiante")
        print("2. Agregar calificación a un estudiante")
        print("3. Mostrar información de un estudiante")
        print("4. Mostrar todos los estudiantes")
        print("5. Salir del programa")

        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                registrar_estudiante()
            case "2":
                agregar_calificacion_estudiante()
            case "3":
                mostrar_info_estudiante()
            case "4":
                mostrar_todos_estudiantes()
            case "5":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Intenta de nuevo.")

menu()