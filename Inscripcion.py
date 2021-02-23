class Carrera():
    def __init__(self ,nombre,codigo):
        self .nombre=nombre
        self .codigo=codigo
        self .materia={}
    def addMateria(self ,materia):
        self .materia[materia.nrc]=materia

class Materia():
    def __init__(self ,nombre,nrc,carrera):
        self .nombre=nombre
        self .nrc=nrc
        self .carrera=carrera
        self .estudiante={}
    def addEstudiante(self ,estudiante):
        self .estudiante[estudiante.iden]=estudiante

class Estudiante():
    def __init__(self ,nombre,iden,materia,par1,par2,par3,prom):
        self .nombre=nombre
        self .iden=iden
        self .materia=materia
        self .par1=par1
        self .par2=par2
        self .par3=par3
        self .prom=prom

    def mostrardatos(self):
        print("\t DATOS DEL ESTUDIANTE ")
        print("Nombre: {}".format(self .nombre))
        print("ID: {}".format(self .iden))
        print("Curso: {}".format(self .materia))


def main():
    civil=Carrera("Ingenieria Civil","CIV001")
    mecds=Materia("Mecanica de suelos","4263",civil)
    civil.addMateria(mecds)
    software=Carrera("Ingenieria de Software","ISOW203")
    poo=Materia("Programacion orientada a objetos","3922",software)
    software.addMateria(poo)
    opmenu = 1
    opmat=1

    while (opmenu != 3):
        print("\t Universidad Mariano Gálvez")
        print("1. Inscribir  Alumno. ")
        print("2. Consultar datos del Alumno. ")
        print("3. Salir.")
        opmenu = int(input("Ingrese la opción: "))

        if opmenu == 1:
            while (opmat != 3):
                print("")
                print("1. Inscribir")
                print("2. Regresar")

                opmat=int(input())

                if opmat == 1:
                    print("")
                    ne = int(input("Ingrese numero de estudiantes: "))
                    if ne <= 8:
                        for i in range (ne):
                            print("Ingresa los datos del alumno ", i + 1)
                            idd = input("ID: ")
                            nom = input("Nombre: ")
                            cur = input("Curso: ")
                            ciclo = input("Ciclo: ")
                            seccion = input("Sección: ")
                            alum1=Estudiante(idd, nom, cur, poo, ciclo, seccion, 0)
                            poo.addEstudiante(alum1)

                    else:
                        print("No mas de 8 alumnos por curso.")
                elif opmat == 2:
                    break


        elif opmenu==2:
                print("\t Consulta de datos")
                opd=1

                while (opd!=3):
                    print(" ")
                    print("1. Visualizar alumnos Inscritos")
                    print("2. Regresar")
                    opd=int(input())

                    if opd == 1:
                        print("Lista de Alumnos Inscritos: ")
                        for m in poo.estudiante.values():
                            print("ID    Alumno   Curso")
                            print(m.nombre, '-', m.iden, '-', m.materia)

                    elif opd == 2:
                        break
        elif opmenu == 3:
                print("SERVICIO FINALIZADO.")
                break

        else:
                print("No existe esta opción")

if __name__ == "__main__":
    main()