from Salarios import *
from Trabajadores import *

dato = Salarios("Tarea_4\junio.dat")
print("Salarios:")
dato.get_final_salaries()
print("--------------------------")
print("Salario por ID:")
dato.get_salario_final("2345")
print("--------------------------")
print(dato.get_empleado_mas_antiguo())
print("--------------------------")
print(dato.get_empleado_mas_nuevo())

#print ( data.to_string() )
#print( data.get_salary( 2345 ) )
