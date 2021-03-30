from xml.dom import minidom
from cola import Cola
from listacircular import *
from matriz import *
from tkinter import *
from tkinter import filedialog
import os
import time
from PIL import Image, ImageTk
nueva_cola = Cola()
lista_matrices = ListaCiruclar()
cont = -1

ventana = Tk()
ventana.title("Bienvenido")
ventana.geometry("800x580")


def refresh(self):
    self.destroy()
    self.__init__()

def cargar(ruta):
    load = Image.open(ruta)
    load = load.resize((350, 450), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    imagen2 = Label(ventana, image=render, width=350, height=450)
    imagen2.image = render
    imagen2.place(x=25, y=100)

def cargar_R(ruta):
    load = Image.open(ruta)
    load = load.resize((350, 450), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    imagen1 = Label(ventana, image=render, width=350, height=450)
    imagen1.image = render
    imagen1.place(x=420, y=100)


def AbrirArchivo():
    file = filedialog.askopenfile(title="abrir")
    ruta = str(file.name)
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


def Grafo(Nombre):
    lista_matrices.Listar(Nombre).graficar()
    cargar('archivos/'+str(Nombre)+'.png')

nm = StringVar()


texto1 = Label(text="Nombre Matriz:")
texto1.place(x=10, y=10)
cajaMatriz = Entry(ventana, font="15", width=10)
cajaMatriz.place(x=10, y=30)

texto2 = Label(text="Fila:")
texto2.place(x=125, y=10)
cajaFila = Entry(ventana, font="15", width=3)
cajaFila.place(x=125, y=30)

texto3 = Label(text="Col:")
texto3.place(x=165, y=10)
cajaColumna = Entry(ventana, font="15", width=3)
cajaColumna.place(x=165, y=30)

texto4 = Label(text="Dimension:")
texto4.place(x=210, y=10)
cajaDimension = Entry(ventana, font="15", width=7)
cajaDimension.place(x=210, y=30)

texto5 = Label(text="Elementos:")
texto5.place(x=290, y=10)
cajaElementos = Entry(ventana, font="15", width=7)
cajaElementos.place(x=290, y=30)

texto6 = Label(text="FilaN:")
texto6.place(x=370, y=10)
cajaFila1 = Entry(ventana, font="15", width=3)
cajaFila1.place(x=370, y=30)

texto7 = Label(text="ColN:")
texto7.place(x=420, y=10)
cajaColumna1 = Entry(ventana, font="15", width=3)
cajaColumna1.place(x=420, y=30)

texto8 = Label(text="Matriz 2:")
texto8.place(x=470, y=10)
cajaM2 = Entry(ventana, font="15", width=10)
cajaM2.place(x=470, y=30)

texto9 = Label(text="Matriz Original:", font="20")
texto9.place(x=20, y=75)

texto10 = Label(text="Matriz Resultante:", font="20")
texto10.place(x=420, y=75)

def RH():
    nom_mat = cajaMatriz.get()
    Grafo(nom_mat)
    lista_matrices.Listar(nom_mat).Rotacion_H()
    cargar_R('archivos/' + str(nom_mat) + '.png')

def RV():
    nom_mat = cajaMatriz.get()
    Grafo(nom_mat)
    lista_matrices.Listar(nom_mat).Rotacion_V()
    cargar_R('archivos/' + str(nom_mat) + '.png')

def Tran():
    nom_mat = cajaMatriz.get()
    Grafo(nom_mat)
    lista_matrices.Listar(nom_mat).Transpuesta()
    cargar_R('archivos/' + str(nom_mat) + '.png')

def LZ():
    nom_mat = cajaMatriz.get()
    Grafo(nom_mat)
    fil = int(cajaFila.get())
    col = int(cajaColumna.get())
    fil1 = int(cajaFila1.get())
    col1 = int(cajaColumna1.get())
    lista_matrices.Listar(nom_mat).Limpiar(fil, col, fil1, col1)
    cargar_R('archivos/' + str(nom_mat) + '.png')

def ALH():
    nom_mat = cajaMatriz.get()
    Grafo(nom_mat)
    fil = int(cajaFila.get())
    col = int(cajaColumna.get())
    can = int(cajaElementos.get())
    lista_matrices.Listar(nom_mat).Agregar_H(fil, col, can)
    cargar_R('archivos/' + str(nom_mat) + '.png')

def ALV():
    nom_mat = cajaMatriz.get()
    Grafo(nom_mat)
    fil = int(cajaFila.get())
    col = int(cajaColumna.get())
    can = int(cajaElementos.get())
    lista_matrices.Listar(nom_mat).Agregar_V(fil, col, can)
    cargar_R('archivos/' + str(nom_mat) + '.png')

def ATR():
    nom_mat = cajaMatriz.get()
    Grafo(nom_mat)
    fil = int(cajaFila.get())
    col = int(cajaColumna.get())
    can = int(cajaDimension.get())
    lista_matrices.Listar(nom_mat).Agregar_Triangulo(fil, col, can)
    cargar_R('archivos/' + str(nom_mat) + '.png')

def ARE():
    nom_mat = cajaMatriz.get()
    Grafo(nom_mat)
    fil = int(cajaFila.get())
    col = int(cajaColumna.get())
    can = str(cajaDimension.get())
    lista_matrices.Listar(nom_mat).Agregar_Rectangulo(fil, col, can)
    cargar_R('archivos/' + str(nom_mat) + '.png')

menuBar = Menu(ventana)

ventana.config(menu=menuBar)

B = Button(text="Abrir Archivo", command=AbrirArchivo, width=10, height=3, bg="orange")
#B.place(x=10, y=10)

B1 = Button(text="Operacion", width=10, height=3, bg="orange")
#B1.place(x=110, y=10)

archivo = Menu(menuBar, tearoff=0)
archivo.add_command(label="Abrir Archivo", command=AbrirArchivo, font="Helvetica 15")

operaciones = Menu(menuBar, tearoff=0,  font="Helvetica 15")
operaciones.add_command(label="Rotacion Horizontal", font="Helvetica 15", command=RH)
operaciones.add_command(label="Rotacion Vertical", font="Helvetica 15", command=RV)
operaciones.add_command(label="Transpuesta", font="Helvetica 15", command=Tran)
operaciones.add_command(label="Limpiar Zona", font="Helvetica 15", command=LZ)
operaciones.add_command(label="Agregar Linea Horizontal", font="Helvetica 15", command=ALH)
operaciones.add_command(label="Agregar Linea Vertical", font="Helvetica 15", command=ALV)
operaciones.add_command(label="Agregar Triangulo", font="Helvetica 15", command=ATR)
operaciones.add_command(label="Agregar Rectangulo", font="Helvetica 15", command=ARE)

repo = Menu(menuBar, tearoff=0)
repo.add_command(label="HTML", font="Helvetica 15")

ayuda = Menu(menuBar, tearoff=0)
ayuda.add_command(label="Documentacion", font="Helvetica 15")
ayuda.add_command(label="Estudiante", font="Helvetica 15")

menuBar.add_cascade(label="Abrir", menu=archivo)
menuBar.add_cascade(label="Operaciones", menu=operaciones)
menuBar.add_cascade(label="Reportes", menu=repo)
menuBar.add_cascade(label="Ayuda", menu=ayuda)

B2 = Button(text="Reporte", width=10, height=3, bg="orange")
#B2.place(x=610, y=10)

B3 = Button(text="Ayuda", width=10, height=3, bg="orange")
#B3.place(x=710, y=10)


place_holder_1 = Label(ventana, bg="gray", width=48, height=28)
place_holder_1.place(x=25, y=100)
place_holder_2 = Label(ventana, bg="gray", width=48, height=28)
place_holder_2.place(x=420, y=100)

"""

lista_matrices.Listar('Matriz_1').graficar()
cargar('archivos/Matriz_1.png')
lista_matrices.Listar('Matriz_1').Rotacion_V()
lista_matrices.Listar('Matriz_1').graficar()
cargar_R('archivos/Matriz_1.png')
"""

ventana.mainloop()
#lista_matrices.Listar('Matriz_1').graficar()
#lista_matrices.Listar('Matriz_1').Transpuesta()
#time.sleep(10)
#lista_matrices.Listar('Matriz_1').graficar()
