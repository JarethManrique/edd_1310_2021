from Colas import  Queue, BoundedPriorityQueue

q1 = Queue()
q1.enqueue(3)
q1.enqueue(33)
q1.enqueue(23)
print(q1.to_string())
print()
print("Prueba 2 de Queue")
print()
c1={"id":1, "nombre":"Mario", "balance":20.5}
c2={"id":2, "nombre":"Diana", "balance":100000}
c3={"id":3, "nombre":"Alex", "balance":999}
c4={"id":4, "nombre":"Gamaliel", "balance":5}
c5={"id":5, "nombre":"Kevin", "balance":500}

atencion = Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)
atencion.enqueue(c4)
atencion.enqueue(c5)
print(atencion.to_string())
sig = atencion.dequeue()
print(f"Bienvenido sr. {sig['nombre']}, en qué podemos servirle el día de hoy")
print(atencion.to_string())
print()
print()
print()
print("PRUEBA DE LAS COLAS CON PRIORIDAD ACOTADA")
print()
maestres = {"Prioridad":4,"Descripcion":"Maestre","Personas":["Juan","Diego"]}
niños = {"Prioridad":2,"Descripcion":"Niños","Personas":["Pedrito","Angel"]}
mecanicos = {"Prioridad":4,"Descripcion":"Mecanicos","Personas":["José","Luis"]}
mujeres = {"Prioridad":3,"Descripcion":"Mujeres","Personas":["Evelyn","Gaby"]}
niñas = {"Prioridad":1,"Descripcion":"Niñas","Personas":["Ahri","Ana"]}

cpa = BoundedPriorityQueue(7)
cpa.enqueue(maestres['Prioridad'],maestres)
cpa.enqueue(niños['Prioridad'],niños)
cpa.enqueue(mecanicos['Prioridad'],mecanicos)
cpa.enqueue(mujeres['Prioridad'],mujeres)
cpa.enqueue(niñas['Prioridad'],niñas)
cpa.to_string()
