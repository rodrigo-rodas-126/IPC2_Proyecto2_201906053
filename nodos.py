class Nodo:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.derecha = None
        self.izquierda = None
        self.arriba = None
        self.abajo = None


class nodoEncabezado:
    def __init__(self, id):
        self.id = id
        self.siguiente = None
        self.anterior = None
        self.accesoNodo = None

class NodoGuardar:
    def __init__(self, Ortogonal):
        self.Ortogonal = Ortogonal