import csv
from ClaseAlumno import Alumno
class ManejadorAlumno:
    __listaAlumno = []
    def __init__(self):
        self.__listaAlumno = []
    def test(self):
        testNombre = 'Marcos'
        testYear = 6
        testDivision = 'B'
        testCantidadDeInasistencias = 7
        testAlumno = Alumno(testNombre,testYear,testDivision,testCantidadDeInasistencias)
        print("TEST REALIZADO EXITOSAMENTE")
    def cargarLista(self):
        archivo = open('Alumnoss.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            nom = fila[0]
            a = int(fila[1])
            div = fila[2]
            cant = int(fila[3])
            Alu = Alumno(nom,a,div,cant)
            self.__listaAlumno.append(Alu)
        archivo.close()
    def listarAlumno(self,anoo,divv):
        for Alumno in self.__listaAlumno:
            if ((Alumno.getAno())==anoo)and((Alumno.getDivision())==divv)and((Alumno.getCantidadInasistencias())>(Alumno.getInasistenciasPermitidas())):
                porcentaje=((Alumno.getCantidadInasistencias())*100)/Alumno.getCantidadTotalDeClases()
                print("{}{:.2f}{}".format((Alumno.getNombre()).ljust(15),porcentaje,'%'))
    def modCantMaxInasistencias(self,max):
        Alumno.InasistenciasPermitidas=max
        print("Nueva cantidad maxima de inasistencias permitidas: ",Alumno.InasistenciasPermitidas)
