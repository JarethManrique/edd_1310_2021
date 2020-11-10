class trabajador:

    def __init__( self, id, nombre, a_paterno, a_materno, hrs_ext, salario, año_cntrto ):
        self.__id = id
        self.__nombre = name
        self.__a_paterno = p_lastname
        self.__a_materno = m_lastname
        self.__hrs_ext = extra_hours
        self.__salario = base_salary
        self.__contrato = contract_year
        self.__antiguedad = 2020 - int(contract_year)

    def to_string( self ):
        return (f"""
        ID -> {self.__id},
        Nombre -> {self.__nombre},
        Apellidos -> {self.__a_paterno} {self.__a_materno},
        Horas Extras -> {self.__hrs_ext},
        Salario Base -> {self.__salario},
        Año de contratación -> {self.__contrato}
        """)

    #getters & setters
    def set_id ( self, id):
        self.__id = id
    def get_id ( self ):
        return self.__id


    def set_nombre ( self, nombre):
        self.__nombre = nombre
    def get_nombre ( self ):
        return self.__nombre


    def set_a_paterno ( self, a_paterno):
        self.__a_paterno = a_paterno
    def get_a_paterno ( self ):
        return self.__a_paterno


    def set_a_materno ( self, a_materno):
        self.__a_materno = a_materno
    def get_a_materno ( self ):
        return self.__a_materno


    def set_hrs_ext ( self, hrs_ext):
        self.__hrs_ext = hrs_ext
    def get_hrs_ext ( self ):
        return int(self.__hrs_ext)


    def set_salario ( self, salario):
        self.__salario = salario
    def get_salario ( self ):
        return int(self.__salario)

    def set_año_cntrto ( self, año_cntrto ):
        self.__contrato = año_cntrto
    def get_año_cntrto ( self ):
        return self.__contrato

    def get_antiguedad(self):
        return self.__antiguedad

    def get_salario_final( self ):
        return float(self.__salario) + (float (self.__hrs_ext) * 276.5  ) + ( float(self.__salario) * 0.03 * self.__antiguedad )
