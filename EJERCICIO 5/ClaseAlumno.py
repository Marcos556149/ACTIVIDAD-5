class Alumno:
    InasistenciasPermitidas = 10
    TotalClases = 55
    __nombre = ''
    __ano = ''
    __division = ''
    __cantidadInasistencias = ''
    def __init__(self,nom='',a='',div='',cant=''):
        self.__nombre = nom
        self.__ano = a
        self.__division = div
        self.__cantidadInasistencias = cant
    def __str__(self):
        return 'Alumno nombre: {}, ano: {}, division: {}, cantidad de inasistencias: {}'.format(self.__nombre,self.__ano,self.__division,self.__cantidadInasistencias)
    def getNombre(self):
        return self.__nombre
    def getAno(self):
        return self.__ano
    def getDivision(self):
        return self.__division
    def getCantidadInasistencias(self):
        return self.__cantidadInasistencias
    @classmethod
    def getInasistenciasPermitidas(cls):
        return cls.InasistenciasPermitidas
    @classmethod
    def getCantidadTotalDeClases(cls):
        return cls.TotalClases

