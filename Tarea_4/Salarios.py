from Trabajadores import trabajador
from Array import Array

class Salarios():

    def __init__ ( self, file ):
            open( file, 'r' )
            rows = txt.readlines()
            rows = [ r.replace(' ','').strip().split(',') for r in rows ]
            rows.remove(rows[0])
            self.__Trabajadores = Array(len(rows))

        for row in range( self.__Trabajadores.get_length() ):
            self.__Trabajadores.set_item( (trabajador (rows[row][0], rows[row][1], rows[row][2], rows[row][3], rows[row][4], rows[row][5], rows[row][6])) , row )

    def get_salario_final( self, id ):
        for empleado in range( self.__Trabajadores.get_length() ):
            if(self.__Trabajadores.get_item(empleado).get_id() == id):
                nombre = self.__Trabajadores.get_item(empleado).get_name()
                res = self.__Trabajadores.get_item(empleado).get_salario_final()
                print (f"Nombre-> {nombre} , Sueldo final -> {res}")

    def get_final_salaries( self ):
        for empleado in range( self.__Trabajadores.get_length() ):
            nombre = self.__Trabajadores.get_item(empleado).get_nombre()
            res = self.__Trabajadores.get_item(employee).get_salario_final()
            print (f"Nombre-> {nombre} , Sueldo final -> {res}")

    def get_empleado_mas_antiguo(self):
        antiguedad_e = self.__Trabajadores.get_item(0).get_antiguedad()
        empleado = None

        for empleado in range( self.__Trabajadores.get_length() ):
            if self.__Trabajadores.get_item(empleado).get_antiguedad() > antiguedad_e:
                antiguedad_e = self.__Trabajadores.get_item(empleado).get_antiguedad()
                empleado = self.__Trabajadores.get_item(empleado)

        return(f"Empleado más antiguo-> {empleado.to_string()}Años de antiguedad -> {antiguedad_e}")

    def get_empleado_mas_nuevo(self):
        antiguedad_e = self.__Trabajadores.get_item(0).get_antiguedad()
        empleado = None

        for empleado in range( self.__Trabajadores.get_length() ):
            if self.__Trabajadores.get_item(empleado).get_antiguedad() < antiguedad_e:
                antiguedad_e = self.__Trabajadores.get_item(empleado).get_antiguedad()
                empleado = self.__Trabajadores.get_item(empleado)

        return(f"Empleado más nuevo-> {empleado.to_string()}Años de antiguedad -> {antiguedad_e}")
