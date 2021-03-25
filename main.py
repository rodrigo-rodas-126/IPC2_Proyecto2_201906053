import os
from xml.dom import minidom
from cola import Cola
from listacircular import *
from matriz import *
nueva_cola = Cola()
lista_matrices = ListaCiruclar()
cont = -1


def AbrirArchivo(ruta):
    nombre_archivo = os.path.basename(ruta)
    xml = minidom.parse(ruta)
    matrices = xml.getElementsByTagName("matriz")
    for matrix in matrices:
        nombre = matrix.getElementsByTagName("nombre")[0]
        filas = matrix.getElementsByTagName("filas")[0]
        columnas = matrix.getElementsByTagName("columnas")[0]
        imagen = matrix.getElementsByTagName("imagen")[0]
        #print(nombre.firstChild.data)
        name = nombre.firstChild.data
        #print(filas.firstChild.data)
        row = int(filas.firstChild.data)
        #print(columnas.firstChild.data)
        col = columnas.firstChild.data
        m = Ortogonal(name, row, col)
        imagen1 = str(imagen.firstChild.data.replace(' ', ''))

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
            for j in range(int(col)):
                valor1 = nueva_cola.desencolar()
                if valor1 == '*':
                    m.insertar(i, j, valor1)
                    #m.recorrerColumnas()
        lista_matrices.AgregarFinal(m)
    #lista_matrices.Recorrer()


AbrirArchivo(r'C:\Users\Rodrigo\Desktop\3er año\IPC2\Laboratorio\Proyect2\Pruebas\entrada.xml')
lista_matrices.Listar('Matriz_1').graficar()
