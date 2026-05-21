estudiantes = []
cursos = []


class Estudiante:
    def __init__(self, nombre_estudiante, apellido, matricula, carrera, id_estudiante):
        self.nombre_estudiante = nombre_estudiante.strip()
        self.apellido = apellido.strip()
        self.matricula = matricula.strip()
        self.carrera = carrera.strip()
        self.id_estudiante = id_estudiante.strip()

    def registrar_estudiante(self):
        try:
            if (
                self.nombre_estudiante == ""
                or self.apellido == ""
                or self.matricula == ""
                or self.carrera == ""
                or self.id_estudiante == ""
            ):
                print("Todos los campos del estudiante son obligatorios.")
                return

            for estudiante in estudiantes:
                if estudiante.id_estudiante == self.id_estudiante:
                    print("Ya existe un estudiante con el mismo id.")
                    return

            estudiantes.append(self)
            print("Estudiante agregado correctamente.")

        except Exception as e:
            print(f"Error al registrar estudiante: {e}")


class Cursos:
    def __init__(self, nombre_curso, codigo, profesor, maximo):
        self.nombre_curso = nombre_curso.strip()
        self.codigo = codigo.strip()
        self.profesor = profesor.strip()
        self.maximo = int(maximo)
        self.alumnos = []

    def cantidad_curso(self):
        return len(self.alumnos)

    def registrar_cursos(self):
        try:
            if (
                self.nombre_curso == ""
                or self.codigo == ""
                or self.profesor == ""
            ):
                print("Todos los campos del curso son obligatorios.")
                return

            if self.maximo <= 0:
                print("El máximo de alumnos debe ser mayor a 0.")
                return

            for curso in cursos:
                if curso.codigo == self.codigo:
                    print("Ya existe un curso con el mismo código.")
                    return

            cursos.append(self)
            print("Curso agregado correctamente.")

        except ValueError:
            print("El máximo de alumnos debe ser un número.")

        except Exception as e:
            print(f"Error al registrar curso: {e}")


class Sistema_cursos:

    def inscripcion(self, id_estudiante, codigo):

        try:
            estudiante = None
            curso = None

            for e in estudiantes:
                if e.id_estudiante == id_estudiante:
                    estudiante = e
                    break

            if estudiante is None:
                print("Estudiante no encontrado.")
                return

            for c in cursos:
                if c.codigo == codigo:
                    curso = c
                    break

            if curso is None:
                print("Curso no encontrado.")
                return

            if curso.cantidad_curso() >= curso.maximo:
                print("Cupo máximo alcanzado.")
                return

            if estudiante in curso.alumnos:
                print("El estudiante ya está inscrito en este curso.")
                return

            curso.alumnos.append(estudiante)
            print(f"{estudiante.nombre_estudiante} fue inscrito correctamente.")

        except Exception as e:
            print(f"Error en la inscripción: {e}")

    def baja(self, id_estudiante, codigo):

        try:
            for c in cursos:

                if c.codigo == codigo:

                    for e in c.alumnos:

                        if e.id_estudiante == id_estudiante:
                            c.alumnos.remove(e)
                            print(f"Se eliminó a {e.nombre_estudiante}.")
                            return

                    print("Ese estudiante no está en este curso.")
                    return

            print("Curso no encontrado.")

        except Exception as e:
            print(f"Error al dar de baja: {e}")

    def mostrar_cursos(self):

        try:
            if not cursos:
                print("No hay cursos registrados.")
                return

            print("\nCursos registrados:\n")

            for c in cursos:

                estado = (
                    "Disponible"
                    if c.cantidad_curso() < c.maximo
                    else "No disponible"
                )

                if c.alumnos:
                    estudiante = ", ".join(
                        e.nombre_estudiante for e in c.alumnos
                    )
                else:
                    estudiante = "Nadie"

                print(f"Curso: {c.nombre_curso}")
                print(f"Profesor: {c.profesor}")
                print(f"Código: {c.codigo}")
                print(f"Estado: {estado}")
                print(f"Alumnos: {estudiante}")
                print("-" * 40)

        except Exception as e:
            print(f"Error al mostrar cursos: {e}")

    def mostrar_estudiantes(self):

        try:
            if not estudiantes:
                print("No hay estudiantes registrados.")
                return

            print("\nEstudiantes registrados:\n")

            for e in estudiantes:

                cursos_inscritos = []

                for c in cursos:
                    if e in c.alumnos:
                        cursos_inscritos.append(c.nombre_curso)

                print(f"Nombre: {e.nombre_estudiante}")
                print(f"Apellido: {e.apellido}")
                print(f"Matrícula: {e.matricula}")
                print(f"Carrera: {e.carrera}")
                print(f"ID: {e.id_estudiante}")

                if cursos_inscritos:
                    print("Cursos inscritos:")
                    for nombre_curso in cursos_inscritos:
                        print(f"- {nombre_curso}")
                else:
                    print("Sin cursos inscritos.")

                print("-" * 40)

        except Exception as e:
            print(f"Error al mostrar estudiantes: {e}")


def main():

    sistema = Sistema_cursos()

    while True:

        try:
            print("\n===== SISTEMA DE CURSOS =====")
            print("1 Agregar estudiante")
            print("2 Agregar curso")
            print("3 Inscribirse")
            print("4 Dar de baja")
            print("5 Mostrar todos los cursos")
            print("6 Mostrar todos los estudiantes")
            print("7 Salir")

            respuesta = input("Ingrese su respuesta: ").strip()

            if respuesta == "1":

                nombre = input("Ingrese su nombre: ")
                apellido = input("Ingrese su apellido: ")
                matricula = input("Ingrese su matrícula: ")
                carrera = input("Ingrese su carrera: ")
                id_estudiante = input("Ingrese su id: ")

                estudiante = Estudiante(
                    nombre,
                    apellido,
                    matricula,
                    carrera,
                    id_estudiante
                )

                estudiante.registrar_estudiante()

            elif respuesta == "2":

                nombre = input("Ingrese el nombre del curso: ")
                codigo = input("Ingrese el código del curso: ")
                profesor = input("Ingrese el nombre del profesor: ")

                try:
                    maximo = int(input("Ingrese el número máximo de alumnos: "))

                except ValueError:
                    print("Debe ingresar un número válido.")
                    continue

                curso = Cursos(
                    nombre,
                    codigo,
                    profesor,
                    maximo
                )

                curso.registrar_cursos()

            elif respuesta == "3":

                id_estudiante = input("Ingrese su id: ").strip()
                codigo = input("Ingrese el código del curso: ").strip()

                sistema.inscripcion(
                    id_estudiante,
                    codigo
                )

            elif respuesta == "4":

                id_estudiante = input("Ingrese su id: ").strip()
                codigo = input("Ingrese el código del curso: ").strip()

                sistema.baja(
                    id_estudiante,
                    codigo
                )

            elif respuesta == "5":

                sistema.mostrar_cursos()

            elif respuesta == "6":

                sistema.mostrar_estudiantes()

            elif respuesta == "7":

                print("Saliendo...")
                break

            else:
                print("Respuesta incorrecta.")

        except KeyboardInterrupt:
            print("\nPrograma interrumpido.")
            break

        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")


main()