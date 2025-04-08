class Alumno:
    def __init__(self, nombre, edad, carrera, calificaciones: list[float] ):  
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = calificaciones
        
        
    def agregar_calificciones(self, nota):

        while True:
            if 0 <= nota <= 100:
                self.calificaciones.append(nota)
                print("Nota agregada correctamente... ")  
                chose = input("¿Desea agregar otra calificación? (s/n): ")
                if chose.lower() != "n":
                    break
                
    
    def promedio(self):
        if len(self.calificaciones) > 0:
            return sum(self.calificaciones) / len(self.calificaciones)
        else:
            return print("No hay calificaciones para calcular el promedio.")
        
    def agregar_alumno(self):
        self.nombre = input("Ingrese su nombre: ")
        while True:
            self.edad = int(input("Ingrese su edad: "))
            if self.edad < 0:
                print("La edad no puede ser negativa.")
            else:
                break
        self.carrera = input("Ingrese su carrera: ")
        
        
    def mostrar_informacion(self,numero=None):
        encabezado = f"\nEstudiante #{numero}" if numero else "\nEstudiante:"
        print(encabezado)
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")
        print(f"Calificaciones: {self.calificaciones}")
        print(f"Promedio: {self.promedio():.2f}")
        


alumno1 = Alumno("", 0, "", [])
print("1. Registrar nuevo estudiante")
print("2. Agregar calificación")
print("3. Mostrar información del estudiante")
print("4. Mostrar toda la información")
print("5. Salir")


chose = int(input("Seleccione una opción: "))
match chose:
    case 1:
        alumno1.agregar_alumno()

                        
    case 2:
        nota = float(input("Ingrese una calificación:"))
        alumno1.agregar_calificciones(nota)
        output(" ")
    case 3:
        alumno1.mostrar_informacion()
    case 4:
        print(alumno1.__dict__)
        output = (" ")

    case 5:
        print("Saliendo del programa...")
        exit()
    case _:
        print("Opción no válida. Intente de nuevo.")

        
alumno1= Alumno(nombre, edad, carrera,calificaciones= []) 
 
                




