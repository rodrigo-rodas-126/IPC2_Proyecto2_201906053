from nodos import Nodo, nodoEncabezado
from encabezado import ListaEncabezado
from tkinter import *


class Ortogonal:
    def __init__(self, nombre, filas, columnas):
        self.eFilas = ListaEncabezado()
        self.eColumnas = ListaEncabezado()
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas

    def insertar(self, fila, columna, valor):
        nuevo = Nodo(fila, columna, valor)

        #insercion por filas
        eFila = self.eFilas.getEncabezado(fila)
        if eFila == None:
            eFila = nodoEncabezado(fila)
            eFila.accesoNodo = nuevo
            self.eFilas.setEncabezado(eFila)
        else:
            if nuevo.columna < eFila.accesoNodo.columna:
                nuevo.derecha = eFila.accesoNodo
                eFila.accesoNodo.izquierda = nuevo
                eFila.accesoNodo = nuevo
            else:
                actual = eFila.accesoNodo
                while actual.derecha != None:
                    if nuevo.columna < actual.derecha.columna:
                        nuevo.derecha = actual.derecha
                        actual.derecha.izquierda = nuevo
                        nuevo.izquierda = actual
                        actual.derecha = nuevo
                        break
                    actual = actual.derecha

                if actual.derecha == None:
                    actual.derecha = nuevo
                    nuevo.izquierda = actual

        # insercion por columnas
        eColumna = self.eColumnas.getEncabezado(columna)
        if eColumna == None:
            eColumna = nodoEncabezado(columna)
            eColumna.accesoNodo = nuevo
            self.eColumnas.setEncabezado(eColumna)
        else:
            if nuevo.fila < eColumna.accesoNodo.fila:
                nuevo.abajo = eColumna.accesoNodo
                eColumna.accesoNodo.arriba = nuevo
                eColumna.accesoNodo = nuevo
            else:
                actual = eColumna.accesoNodo
                while actual.abajo != None:
                    if nuevo.fila < actual.abajo.fila:
                        nuevo.abajo = actual.abajo
                        actual.abajo.arriba = nuevo
                        nuevo.arriba = actual
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo

                if actual.abajo == None:
                    actual.abajo = nuevo
                    nuevo.arriba = actual

    def recorrerFilas(self):
        eFila = self.eFilas.primero
        print('\n==================================================')
        while eFila != None:
            actual = eFila.accesoNodo
            print("\nFila "+str(actual.fila))
            print("Columna  Valor")
            while actual != None:
                print(str(actual.columna)+"        "+actual.valor)
                actual = actual.derecha

            eFila = eFila.siguiente
        print('\n==================================================')

    def recorrerColumnas(self):
        eColumna = self.eColumnas.primero
        print('\n==================================================')
        while eColumna != None:
            actual = eColumna.accesoNodo
            print('\nColumna '+str(actual.columna))
            print('Fila   Valor')
            while actual != None:
                print(str(actual.fila)+"      "+actual.valor)
                actual = actual.abajo
            eColumna = eColumna.siguiente
        print('\n==================================================')

    def Rotacion_H(self):
        pass

    def Rotacion_V(self):
        pass

    def Transpuesta(self):
        pass

    def Limpiar(self):
        pass
    
    def Agregar_H(self):
        pass

    def Agregar_V(self):
        pass

    def Agregar_Rectangulo(self):
        pass

    def Agregar_Triangulo(self):
        pass

    def graficar(self):
        """
        for i in range(10):
            try:
                eFila = self.eFilas.getEncabezado(i)
                print('Fila:' + str(eFila.accesoNodo.fila))
            except AttributeError:
                print('Fila:'+str(i)+' Inexistente')
                #for j in range(10):
                #    print('Nodo Columna Inexistente')
        print('\n')

        for j in range(10):
            try:
                eCol = self.eColumnas.getEncabezado(j)
                print('Col:' + str(eCol.accesoNodo.columna))
            except AttributeError:
                print('Col:'+str(j)+' Inexistente')
                #for j in range(10):
                #    print('Nodo Columna Inexistente')
        """
        ventana = Tk()
        ventana.title("Bienvenido")

        mapa = []
        for i in range(int(self.filas)):
            mapa.append(list(' '*int(self.columnas)))
        print(mapa)

        eFila = self.eFilas.primero
        #print(op[0])
        while eFila != None:
            actual = eFila.accesoNodo
            print("\nFila " + str(actual.fila))
            print("Columna  Valor")
            while actual != None:
                print(str(actual.columna) + "        " + actual.valor)
                mapa[int(actual.fila)][int(actual.columna)] = actual.valor
                imagen1 = Label(ventana, bg="blue").grid(row=str(actual.fila), column=str(actual.columna))
                actual = actual.derecha

            eFila = eFila.siguiente

        print(mapa)
        ventana.mainloop()


"""
m=Ortogonal('Matriz_1', 10, 10)
m.insertar(3, 1, "*")
m.insertar(1, 1, "*")
m.insertar(1, 3, "*")
m.insertar(0, 2, "*")
m.insertar(5, 5, "*")
m.recorrerColumnas()
m.recorrerFilas()
"""
