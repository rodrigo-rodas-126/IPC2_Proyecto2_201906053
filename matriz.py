from nodos import Nodo, nodoEncabezado
from encabezado import ListaEncabezado
from tkinter import *
import os


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

    def devolverFilas(self):
        Valores = {}
        eFila = self.eFilas.primero
        #print('\n==================================================')
        while eFila != None:
            actual = eFila.accesoNodo
            #print("\nFila "+str(actual.fila))
            Valores[actual.fila] = []
            #print("Columna  Valor")
            while actual != None:
                #print(str(actual.columna)+"        "+actual.valor)
                Valores[actual.fila].append(actual.columna)
                actual = actual.derecha
            eFila = eFila.siguiente
        #print('\n==================================================')
        #print(Valores)
        return Valores

    def devolverColumnas(self):
        Valores={}
        eColumna = self.eColumnas.primero
        #print('\n==================================================')
        while eColumna != None:
            actual = eColumna.accesoNodo
            #print('\nColumna '+str(actual.columna))
            Valores[actual.columna] = []
            #print('Fila   Valor')
            while actual != None:
                #print(str(actual.fila)+"      "+actual.valor)
                Valores[actual.columna].append(actual.fila)
                actual = actual.abajo
            eColumna = eColumna.siguiente
        #print('\n==================================================')
        #print(Valores)
        return Valores

    def Rotacion_H(self):
        Datos = self.devolverFilas()
        self.Borrar()
        for v in Datos:
            #print(v)
            cambio_fila = int(self.filas) - v
            for b in Datos[v]:
                #print(b)
                self.insertar(cambio_fila - 1, int(b), '*')
        self.graficar()


    def Rotacion_V(self):
        Datos = self.devolverColumnas()
        self.Borrar()
        for v in Datos:
            # print(v)
            cambio_col = int(self.columnas) - v
            for b in Datos[v]:
                # print(b)
                self.insertar(int(b), cambio_col - 1, '*')
        self.graficar()

    def Transpuesta(self):
        Datos = self.devolverFilas()
        self.Borrar()
        for v in Datos:
            # print(v)
            cambio_fila = int(self.filas) - v
            for b in Datos[v]:
                # print(b)
                self.insertar(int(b), cambio_fila - 1, '*')
        self.Rotacion_V()
        self.graficar()

    def Borrar_Nodo(self, fila1, columna1):
        eFila = self.eFilas.primero
        while eFila != None:
            actual = eFila.accesoNodo
            while actual != None:
                if actual.fila == fila1 and actual.columna == columna1:
                    if actual.izquierda == None:
                        if actual.derecha == None:
                            eFila.accesoNodo = None
                        else:
                            if eFila.accesoNodo != actual:
                                actual.izquierda.derecha = actual.derecha
                            else:
                                eFila.accesoNodo = actual.derecha
                                if actual.abajo != None:
                                    if actual.arriba == None:
                                        #if self.eColumnas.getEncabezado(actual.columna).accesoNodo == actual:
                                        #    self.eColumnas.getEncabezado(actual.columna).accesoNodo = actual.abajo
                                        efCol = self.eFilas.getEncabezado(actual.columna).accesoNodo
                                        efCol.accesoNodo = actual.abajo

                                    else:
                                        actual.abajo.arriba = actual.arriba
                                        actual.arriba.abajo = actual.abajo
                                else:
                                    if actual.arriba != None:
                                        actual.arriba.abajo = None

                    else:
                        if actual.derecha != None:
                            actual.izquierda.derecha = actual.derecha
                            actual.derecha.izquierda = actual.izquierda
                            if actual.abajo != None:
                                if actual.arriba != None:
                                    actual.abajo.arriba = actual.arriba
                                    actual.arriba.abajo = actual.abajo
                                else:
                                    if self.eColumnas.getEncabezado(actual.columna).accesoNodo == actual:
                                        self.eColumnas.getEncabezado(actual.columna).accesoNodo = None
                            else:
                                if actual.arriba != None:
                                    actual.arriba.abajo = None
                                else:
                                    self.eColumnas.getEncabezado(actual.columna).accesoNodo = None
                        else:
                            actual.izquierda.derecha = None
                    return
                actual = actual.derecha
            eFila = eFila.siguiente

    def Limpiar(self, fila, columna, fila1, columna1):
        if int(columna1) >= int(self.columnas) or int(columna) >= int(self.columnas) or int(fila1) >= int(self.filas) or int(fila) >= int(self.filas):
            raise IndexError
        elif fila1 < fila or columna1 < columna:
            raise IndexError

        iFila = abs(fila1 - fila)
        iCol = abs(columna1 - columna)

        saveCol = columna1

        fila1 += 1
        #self.Borrar_Nodo(fila1, columna1)
        for u in range(iFila + 1):
            fila1 -= 1
            #print('Fila: '+str(fila1))
            columna1 = saveCol
            columna1 += 1
            for k in range(iCol + 1):
                columna1 -= 1
                #print('Col: '+str(columna1))
                self.Borrar_Nodo(fila1, columna1)
        self.graficar()
    
    def Agregar_H(self, fila, columna, longitud):
        if (longitud + int(columna)) > int(self.columnas):
            raise IndexError
        columna -= 1
        for a in range(longitud):
            columna += 1
            self.insertar(fila, columna, '*')
        self.graficar()

    def Agregar_V(self, fila, columna, longitud):
        if (longitud + int(fila)) > int(self.filas):
            raise IndexError
        fila -= 1
        for a in range(longitud):
            fila += 1
            self.insertar(fila, columna, '*')
        self.graficar()

    def Agregar_Rectangulo(self, fila, columna, expresion):
        nexpresion = expresion.split('x')
        largo = int(nexpresion[0])
        alto = int(nexpresion[1])
        if (largo + int(columna)) > int(self.columnas) or (alto + int(fila)) > int(self.filas):
            raise IndexError
        # Agregando Primer Pilar Horizontal
        self.Agregar_H(fila, columna, largo)
        # Agregando Segundo Pilar Horizontal
        self.Agregar_H((fila + alto) - 1, columna, largo)
        # Agregando Primer Pilar Vertical
        self.Agregar_V(fila, columna, alto)
        # Agregando Segundo Pilar Vertical
        self.Agregar_V(fila, (columna + largo) - 1, alto)
        self.graficar()

    def Agregar_Triangulo(self, fila, columna, dimension):
        # Agregando la Altura del Tringulo
        self.Agregar_V(fila, columna, dimension)
        # Agregando la Base del Tringulo
        self.Agregar_H(fila + (dimension - 1), columna, dimension)
        # Agregando la Diagonal del Tringulo
        contador_fila = int(fila) - 1
        contador_col = int(columna) - 1
        for m in range(dimension):
            contador_col += 1
            contador_fila += 1
            self.insertar(contador_fila, contador_col, '*')
        self.graficar()

    def Borrar(self):
        self.eFilas = ListaEncabezado()
        self.eColumnas = ListaEncabezado()

    def graficar(self):
        #ventana = Tk()
        #ventana.title("Bienvenido")

        mapa = []
        for i in range(int(self.filas)):
            mapa.append(list(' '*int(self.columnas)))
        #print(mapa)

        eFila = self.eFilas.primero
        #print(op[0])
        while eFila != None:
            actual = eFila.accesoNodo
            #print("\nFila " + str(actual.fila))
            #print("Columna  Valor")
            while actual != None:
                #print(str(actual.columna) + "        " + actual.valor)
                mapa[int(actual.fila)][int(actual.columna)] = actual.valor
                #imagen1 = Label(ventana, bg="blue").grid(row=str(actual.fila), column=str(actual.columna))
                actual = actual.derecha
            eFila = eFila.siguiente

        """
        imagen1 = Label(ventana, text=str('ID'), bd=3, width=2, height=2).grid(row=str(0), column=str(0))

        for la in range(int(self.filas)):
            imagen1 = Label(ventana, text=str(la), bd=3, width=2, height=2).grid(row=str(la+1), column=str(0))

        for lu in range(int(self.columnas)):
            imagen1 = Label(ventana, text=str(lu), bd=3, width=2, height=2).grid(row=str(0), column=str(lu+1))

        cont_fil = -1
        cont_col = -1
        for valor in mapa:
            cont_fil += 1
            cont_col = -1
            for val in valor:
                cont_col += 1
                if val == '*':
                    imagen1 = Label(ventana, bg="blue", width=2, height=2, bd=2).grid(row=str(int(cont_fil)+1), column=str(int(cont_col)+1))
                else:
                    imagen1 = Label(ventana, bg="white", width=2, height=2, bd=2).grid(row=str(int(cont_fil)+1), column=str(int(cont_col)+1))
        #print(mapa)
        #ventana.mainloop()
        """

        with open('archivos/'+str(self.nombre)+'.dot', 'w') as re:
            re.write('digraph G { bgcolor="white"'+'\n')
            re.write('node [shape=plain]' + '\n')
            re.write('a0 [label=<' + '\n')
            re.write('<table border="0" cellborder="1" cellspacing="2" cellpadding="10">' + '\n')
            #Encabezados
            re.write('<tr>' + '\n')
            re.write('<td>ID</td>' + '\n')
            for an in range(int(self.columnas)):
                re.write('<td>'+str(an)+'</td>' + '\n')
            re.write('</tr>' + '\n')
            
            cont = -1
            for valor in mapa:
                cont += 1
                re.write('<tr>' + '\n')
                re.write('<td>'+str(cont)+'</td>' + '\n')
                for val in valor:
                    if val == '*':
                        re.write('<td bgcolor="black"> </td>' + '\n')
                    else:
                        re.write('<td bgcolor="white"> </td>' + '\n')
                re.write('</tr>' + '\n')
            re.write('</table>>];' + '\n')
            re.write('}' + '\n')
            re.close()
        os.system('dot -T png '+'archivos/'+str(self.nombre)+'.dot'+' -o '+'archivos/'+str(self.nombre)+'.png')
