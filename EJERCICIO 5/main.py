from ManejadorAlumno import ManejadorAlumno
if __name__=='__main__':
    lista = ManejadorAlumno()
    lista.cargarLista()
    lista.test()
    while True:
        print("_____MENU DE OPCIONES_____")
        print("[1]...Listar nombre y porcentaje de inasistencias de alumnos que superar la maxima de inasistencias permitidas")
        print("[2]...Modificar cantidad maxima de inasistencias permitidas")
        print("[0]...Salir")
        try:
            op = int(input('Selecciona una opcion: '))
            if op in range(3):
                if op == 1:
                    anoo=int(input('Ingrese año: '))
                    divv=input('Ingrese divivion: ')
                    print("Alumno         Porcentaje")
                    lista.listarAlumno(anoo,divv)
                if op == 2:
                    max=int(input('Ingrese nueva cantidad maxima de inasistencias permitidas: '))
                    lista.modCantMaxInasistencias(max)
                if op == 0:
                    print("_____MENU FINALIZADO_____")
                    break
            else:
                print("ERROR, solo puede ingresar numeros del 1 al 3")
        except ValueError:
            print("ERROR,ingrese solamente numeros")
