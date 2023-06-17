#Anchundia Asencio Alex
#Castañeda Arteaga Maria
#Macias Diaz Luis
#Orrala Macias Tommy
from docente import Docente
from estudiante import Estudiante
from libro import Libro
from revista import Revista
from pedido import Pedido

d1 = Docente(cedula='0956941127', nombre='CHRISTIAN', apellido='MERIZALDE', email='cmerizalde@gmail.com',
             telefono='098898420', direccion='ESTEROS', numero_libros=0, activo=True, carrera='GIG',
             titulo_3er_nivel='ING', titulo_4to_nivel=',MAE')
d2 = Docente(cedula='0917236863', nombre='GUILLERMO', apellido='VALAREZO', email='gvalarezo@gmail.com',
             telefono='0982222920', direccion='LA JOYA', numero_libros=0, activo=True, carrera='GIG',
             titulo_3er_nivel='ING', titulo_4to_nivel=',MAE')

print(d1)
print(d2)

# Estudiantes
e1 = Estudiante(cedula='0930678289', nombre='Alex', apellido='Anchundia', email='aachundia@gmail.com',
                telefono='0997583057', direccion='Posorja', numero_libros=0, activo=True, carrera='GIG',
                nivel=3)
e2 = Estudiante(cedula='0930629989', nombre='Maria', apellido='Castañeda', email='mcastaneda@gmail.com',
                telefono='0945683057', direccion='Duran', numero_libros=0, activo=True, carrera='GIG',
                nivel=3)
e3 = Estudiante(cedula='0930621289', nombre='Luis', apellido='Macias', email='lmacias@gmail.com',
                telefono='0997993057', direccion='Trinitaria', numero_libros=0, activo=True, carrera='GIG',
                nivel=3)
e4 = Estudiante(cedula='0988621289', nombre='Tommy', apellido='Orrala', email='torrala@gmail.com',
                telefono='0997773057', direccion='Suburbio', numero_libros=0, activo=True, carrera='GIG',
                nivel=3)

print(e1)
print(e2)
print(e3)
print(e4)


l1 = Libro(codigo='1', autor='', titulo='', anio=2019, editorial='', disponible=True, cantidad_disponible=10,tipo_pasta='')
l2 = Libro(codigo='1', autor='', titulo='', anio=2019, editorial='', disponible=True, cantidad_disponible=10,tipo_pasta='')
print(l1)

r1 = Revista(codigo='1', autor='JSCA', titulo='REVISTA DE SOFTWARE', anio=2019, editorial='UG', disponible=True, cantidad_disponible=12,tipo='VIRTUAL')
print(r1)

pedido1 = Pedido(id='095412447784', solicitante='Luis Macias', lista_material='DESARROLLO EN PYTHON',
                 fecha_prestamo='10/Junio/2023', fecha_devolucion='15/Junio/2023')
print(pedido1)