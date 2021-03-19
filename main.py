from ortogonal import *
import os
from xml.dom import minidom
from cola import Cola
from listacircular import *
from matriz import *
nueva_cola = Cola()
lista_matrices = ListaCiruclar()
cont = -1


def AbrirArchivo():
    ruta = r'C:\Users\Rodrigo\Desktop\3er año\IPC2\Laboratorio\Proyect2\Pruebas\entrada.xml'
    nombre_archivo = os.path.basename(ruta)
    xml = minidom.parse(ruta)
    matrices = xml.getElementsByTagName("matriz")
    for matrix in matrices:
        nombre = matrix.getElementsByTagName("nombre")[0]
        filas = matrix.getElementsByTagName("filas")[0]
        columnas = matrix.getElementsByTagName("columnas")[0]
        imagen = matrix.getElementsByTagName("imagen")[0]
        print(nombre.firstChild.data)
        name = nombre.firstChild.data
        print(filas.firstChild.data)
        row = int(filas.firstChild.data)
        print(columnas.firstChild.data)
        col = columnas.firstChild.data
        imagen1 = str(imagen.firstChild.data.replace(' ', ''))
        general = linked_list1()
        for asn in range(1, int(row)*int(col) + int(col)):
            caracter = imagen1[asn]
            if caracter == '\n':
                continue
            else:
                if caracter == '-':
                    nueva_cola.encolar(' ')
                else:
                    nueva_cola.encolar(caracter)
        for i in range(int(row)):
            a = linked_list()
            for j in range(int(col)):
                valor1 = nueva_cola.desencolar()
                a.insertar(valor1)
            general.insertar(a)
        print(general.string())
        lista_matrices.AgregarFinal(Matriz(str(name), int(row), int(col), general))
    lista_matrices.Recorrer()
