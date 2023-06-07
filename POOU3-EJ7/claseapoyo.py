from clasepersonal import Personal

class Apoyo(Personal):
    __categotria=int

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad,categoria):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad)
        self.__categotria=categoria

    def getCategoria(self):
        return self.__categotria
    def getSueldobasico(self):
        return super().getSueldobasico()
    def getAntiguedad(self):
        return super().getAntiguedad()
    def getApellido(self):
        return super().getApellido()
    def getCuil(self):
        return super().getCuil()
    def getNombre(self):
        return super().getNombre()

    def getSueldo(self):
        sueldo=0
        if int(self.getCategoria())>=1 and int(self.getCategoria())<=10:
            porcentaje=10
        elif int(self.getCategoria())>=11 and int(self.getCategoria())<=20:
            porcentaje=20
        elif int(self.getCategoria())>=21 and int(self.getCategoria())<=22:
            porcentaje=30
        sueldo=float(self.getSueldobasico()+float(self.getAntiguedad()*self.getSueldobasico()/100))
        sueldo=float(sueldo+porcentaje*sueldo/100)    
        return sueldo

    def __str__(self):
        return super().__str__()+'Categoria:{}'.format(self.__categotria)    