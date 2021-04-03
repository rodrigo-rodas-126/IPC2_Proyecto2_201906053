from xml.dom import minidom
from cola import Cola
from listacircular import *
from matriz import *
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import time
import webbrowser
from PIL import Image, ImageTk
nueva_cola = Cola()
lista_matrices = ListaCiruclar()
cont = -1

reporte = []
Bandera = False

def Documentacion():
    webbrowser.open(os.getcwd() + '/Docu/Ensayo_IPC2.pdf')

def GenerarReporte():
    if len(reporte) == 0:
        messagebox.showwarning('Donde Te Sentaste', message="No se a realizado ninguna operacion")
        return
    else:
        with open('archivos/Reporte.html', 'w') as re:
            re.write('<html>' + '\n')
            re.write('<head>' + '\n')
            re.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">' + '\n')
            re.write('</head>' + '\n')
            re.write('<body>' + '\n')
            re.write('<center>' + '\n')
            re.write('<table class="table table-hover table-striped">' + '\n')
            re.write('<thead>' + '\n')
            re.write('<tr>' + '\n')
            re.write('<th>No.</th>' + '\n')
            re.write('<th>Informe Proceso</th>' + '\n')
            re.write('</tr>' + '\n')
            re.write('</thead>' + '\n')
            re.write('<tbody>' + '\n')
            for lin in range(len(reporte)):
                re.write('<tr class="bg-light">' + '\n')
                re.write('<th class="row">'+str(lin)+'</th>' + '\n')
                re.write('<td>'+str(reporte[lin])+'</td>' + '\n')
                re.write('</tr>' + '\n')
            re.write('</tbody>' + '\n')
            re.write('</table>' + '\n')
            re.write('</center>' + '\n')
            re.write('</body>' + '\n')
            re.write('</html>' + '\n')
            re.close()
        webbrowser.open(os.getcwd() + '/archivos' + '/Reporte.html')

ventana = Tk()
ventana.title("Bienvenido")
ventana.geometry("800x580")

def jojos():
    ventana.geometry("1170x580")

def jojos1():
    ventana.geometry("800x580")

def refresh(self):
    self.destroy()
    self.__init__()

def DatosMi():
    messagebox.showinfo("Mis Datos UwU", message="Jose Rodrigo Rodas Palencia \n 201906053 \n IPC2 \n Seccion: E")

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

def cargar_R1(ruta):
    load = Image.open(ruta)
    load = load.resize((350, 450), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    imagen3 = Label(ventana, image=render, width=350, height=450)
    imagen3.image = render
    imagen3.place(x=800, y=100)


def AbrirArchivo():
    file = filedialog.askopenfile(title="abrir")
    ruta = str(file.name)
    nombre_archivo = os.path.basename(ruta)
    xml = minidom.parse(ruta)
    matrices = xml.getElementsByTagName("matriz")
    for matrix in matrices:
        contador_vacios = 0
        contador_llenos = 0
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
                    contador_vacios += 1
                    nueva_cola.encolar(' ')
                else:
                    contador_llenos += 1
                    nueva_cola.encolar(caracter)
        for i in range(int(row)):
            for j in range(int(col)):
                valor1 = nueva_cola.desencolar()
                if valor1 == '*':
                    m.insertar(i, j, valor1)

        reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - ' + str(name) + ' - Espacios Llenos: ' + str(contador_llenos) + ' - Espacios Vacios: ' + str(contador_vacios))
        lista_matrices.AgregarFinal(m)
    Bandera = True
    messagebox.showinfo(message="Archivo Cargado con Exito")
    #lista_matrices.Recorrer()


def Grafo(Nombre):
    lista_matrices.Listar(Nombre).graficar()
    cargar('archivos/'+str(Nombre)+'.png')

def Grafo2(Nombre):
    lista_matrices.Listar(Nombre).graficar()
    cargar_R1('archivos/'+str(Nombre)+'.png')

def Grafo1(Nombre):
    lista_matrices.Listar(Nombre).graficar()
    cargar_R('archivos/'+str(Nombre)+'.png')

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

texto11 = Label(text="Matriz Original 2:", font="20")
texto11.place(x=800, y=75)

def RH():
    jojos1()
    nom_mat = cajaMatriz.get()
    try:
        Grafo(nom_mat)
    except:
        messagebox.showwarning(message='Error')
        reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
            time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
            time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
            nom_mat) + ' - Error: ' + 'Matriz Inexistente')
        return
    lista_matrices.Listar(nom_mat).Rotacion_H()
    cargar_R('archivos/' + str(nom_mat) + '.png')
    reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
        time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
        time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
        nom_mat) + ' - Operacion: ' + 'Rotacion Horizontal')

def RV():
    jojos1()
    nom_mat = cajaMatriz.get()
    try:
        Grafo(nom_mat)
    except:
        messagebox.showwarning(message='Error')
        reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
            time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
            time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
            nom_mat) + ' - Error: ' + 'Matriz Inexistente')
        return
    lista_matrices.Listar(nom_mat).Rotacion_V()
    cargar_R('archivos/' + str(nom_mat) + '.png')
    reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
        time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
        time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
        nom_mat) + ' - Operacion: ' + 'Rotacion Vertical')

def Tran():
    jojos1()
    nom_mat = cajaMatriz.get()
    try:
        Grafo(nom_mat)
    except:
        messagebox.showwarning(message='Error')
        reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
            time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
            time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
            nom_mat) + ' - Error: ' + 'Matriz Inexistente')
        return
    lista_matrices.Listar(nom_mat).Transpuesta()
    cargar_R('archivos/' + str(nom_mat) + '.png')
    reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
        time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
        time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
        nom_mat) + ' - Operacion: ' + 'Transpuesta')

def LZ():
    jojos1()
    nom_mat = cajaMatriz.get()
    try:
        Grafo(nom_mat)
    except:
        messagebox.showwarning(message='Error')
        reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
            time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
            time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
            nom_mat) + ' - Error: ' + 'Matriz Inexistente')
        return
    fil = int(cajaFila.get())
    col = int(cajaColumna.get())
    fil1 = int(cajaFila1.get())
    col1 = int(cajaColumna1.get())
    try:
        lista_matrices.Listar(nom_mat).Limpiar(fil, col, fil1, col1)
    except:
        messagebox.showwarning(message='Error')
        reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
            time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
            time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
            nom_mat) + ' - Error: ' + 'Index Error')
        return
    reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
        time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
        time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
        nom_mat) + ' - Operacion: ' + 'Limpiar Zona' + 'Columna:' + str(fil) + ' Fila:' + str(col) + ' Hasta ' + 'Columna:' + str(col1) + ' Fila:' + str(fil1))
    cargar_R('archivos/' + str(nom_mat) + '.png')

def ALH():
    jojos1()
    nom_mat = cajaMatriz.get()
    try:
        Grafo(nom_mat)
    except:
        messagebox.showwarning(message='Error')
        reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
            time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
            time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
            nom_mat) + ' - Error: ' + 'Matriz Inexistente')
        return
    fil = int(cajaFila.get())
    col = int(cajaColumna.get())
    can = int(cajaElementos.get())
    try:
        lista_matrices.Listar(nom_mat).Agregar_H(fil, col, can)
    except:
        messagebox.showwarning(message='Error')
        reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
            time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
            time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
            nom_mat) + ' - Error: ' + 'Index Error')
        return
    reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
        time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
        time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
        nom_mat) + ' - Operacion: ' + 'Agregar Linea Horizontal' + 'Columna:' + str(col) + ' Fila:' + str(fil) + ' Elementos: ' + str(can))
    cargar_R('archivos/' + str(nom_mat) + '.png')

def ALV():
    jojos1()
    nom_mat = cajaMatriz.get()
    Grafo(nom_mat)
    fil = int(cajaFila.get())
    col = int(cajaColumna.get())
    can = int(cajaElementos.get())
    try:
        lista_matrices.Listar(nom_mat).Agregar_V(fil, col, can)
    except:
        messagebox.showwarning(message='Error')
        reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
            time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
            time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
            nom_mat) + ' - Error: ' + 'Index Error')
        return
    reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
        time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
        time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
        nom_mat) + ' - Operacion: ' + 'Agregar Linea Vertical' + 'Columna:' + str(col) + ' Fila:' + str(fil) + ' Elementos: ' + str(can))
    cargar_R('archivos/' + str(nom_mat) + '.png')

def ATR():
    jojos1()
    nom_mat = cajaMatriz.get()
    Grafo(nom_mat)
    fil = int(cajaFila.get())
    col = int(cajaColumna.get())
    can = int(cajaDimension.get())
    try:
        lista_matrices.Listar(nom_mat).Agregar_Triangulo(fil, col, can)
    except:
        messagebox.showwarning(message='Error')
        reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
            time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
            time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
            nom_mat) + ' - Error: ' + 'Index Error')
        return
    reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
        time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
        time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
        nom_mat) + ' - Operacion: ' + 'Agregar Triangulo Rectangulo' + 'Columna:' + str(col) + ' Fila:' + str(fil) + ' Dimension: ' + str(can))
    cargar_R('archivos/' + str(nom_mat) + '.png')

def ARE():
    jojos1()
    nom_mat = cajaMatriz.get()
    try:
        Grafo(nom_mat)
    except:
        messagebox.showwarning(message='Error')
        reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
            time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
            time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
            nom_mat) + ' - Error: ' + 'Matriz Inexistente')
        return
    fil = int(cajaFila.get())
    col = int(cajaColumna.get())
    can = str(cajaDimension.get())
    try:
        lista_matrices.Listar(nom_mat).Agregar_Rectangulo(fil, col, can)
    except:
        messagebox.showwarning(message='Error')
        reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
            time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
            time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
            nom_mat) + ' - Error: ' + 'Index Error')
        return
    reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
        time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
        time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
        nom_mat) + ' - Operacion: ' + 'Agregar Rectangulo' + 'Columna:' + str(col) + ' Fila:' + str(fil) + ' Dimension:' + str(can))
    cargar_R('archivos/' + str(nom_mat) + '.png')

def BorrarUnNodo():
    jojos1()
    nom_mat = cajaMatriz.get()
    try:
        Grafo(nom_mat)
    except:
        messagebox.showwarning(message='Error')
        reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
            time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
            time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
            nom_mat) + ' - Error: ' + 'Matriz Inexistente')
        return
    fil = int(cajaFila.get())
    col = int(cajaColumna.get())
    try:
        lista_matrices.Listar(nom_mat).Borrar_Nodo(fil, col)
    except:
        messagebox.showwarning(message='Error')
        reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
            time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
            time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
            nom_mat) + ' - Error: ' + 'Index Error')
        return
    reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
        time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
        time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
        nom_mat) + ' - Operacion: ' + 'Borrar Nodo')
    cargar_R('archivos/' + str(nom_mat) + '.png')

def GraficarOriginal():
    jojos1()
    nom_mat = cajaMatriz.get()
    nom_mat_1 = cajaM2.get()
    try:
        Grafo(nom_mat)
        if nom_mat_1 != ' ':
            try:
                Grafo2(nom_mat_1)
                jojos()
            except:
                pass
    except:
        messagebox.showwarning(message='Error')
        reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
            time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
            time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
            nom_mat) + ' - Error: ' + 'Matriz Inexistente')
        return

def Union():
    jojos()
    nom_mat = cajaMatriz.get()
    nom_mat_1 = cajaM2.get()
    try:
        Datos1 = lista_matrices.Listar(nom_mat).devolverFilas()
        Datos2 = lista_matrices.Listar(nom_mat_1).devolverFilas()

        Grafo(nom_mat)
        Grafo2(nom_mat_1)
    except:
        reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
            time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
            time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Error: Matriz Inexistente')
        return
    nombre = 'Matriz_U'
    fil = lista_matrices.Listar(nom_mat).filas
    col = lista_matrices.Listar(nom_mat).columnas
    new_m = Ortogonal(str(nombre), int(fil), int(col))

    for v in Datos1:
        for b in Datos1[v]:
            new_m.insertar(v, b, '*')

    for e in Datos2:
        for c in Datos2[e]:
            if e > int(fil) or c > int(col):
                reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
                    time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
                    time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
                    nom_mat) + ', ' + str(nom_mat_1) + ' - Error: ' + 'Nodos fuera de index')
                return
            else:
                new_m.insertar(e, c, '*')

    lista_matrices.AgregarFinal(new_m)
    Grafo1(nombre)

    reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
        time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
        time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
        nom_mat) + ', ' + str(nom_mat_1) + ' - Operacion: ' + 'Union')


def Union1():
    jojos()
    nom_mat = 'Matriz_D'
    nom_mat_1 = 'Matriz_D1'
    try:
        Datos1 = lista_matrices.Listar(nom_mat).devolverFilas()
        Datos2 = lista_matrices.Listar(nom_mat_1).devolverFilas()

        Grafo(nom_mat)
        Grafo2(nom_mat_1)
    except:
        reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
            time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
            time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Error: Matriz Inexistente')
        return
    nombre = 'Matriz_DS'
    fil = lista_matrices.Listar(nom_mat).filas
    col = lista_matrices.Listar(nom_mat).columnas
    new_m = Ortogonal(str(nombre), int(fil), int(col))

    for v in Datos1:
        for b in Datos1[v]:
            new_m.insertar(v, b, '*')

    for e in Datos2:
        for c in Datos2[e]:
            if e > int(fil) or c > int(col):
                reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
                    time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
                    time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
                    nom_mat) + ', ' + str(nom_mat_1) + ' - Error: ' + 'Nodos fuera de index')
                return
            else:
                new_m.insertar(e, c, '*')

    lista_matrices.AgregarFinal(new_m)
    Grafo1(nombre)

    reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
        time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
        time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
        nom_mat) + ', ' + str(nom_mat_1) + ' - Operacion: ' + 'Union')

def Interseccion():
    jojos()
    nom_mat = cajaMatriz.get()
    nom_mat_1 = cajaM2.get()
    try:
        Datos1 = lista_matrices.Listar(nom_mat).devolverFilas()
        Datos2 = lista_matrices.Listar(nom_mat_1).devolverFilas()

        Grafo(nom_mat)
        Grafo2(nom_mat_1)
    except:
        reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
            time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
            time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Error: Matriz Inexistente')
        return
    nombre = 'Matriz_I'
    fil = lista_matrices.Listar(nom_mat).filas
    col = lista_matrices.Listar(nom_mat).columnas
    new_m = Ortogonal(str(nombre), int(fil), int(col))

    for j in range(int(fil)):
        try:
            col1 = Datos1[j]
            col2 = Datos2[j]
            try:
                for m in col1:
                    if m in col2:
                        new_m.insertar(j, int(m), '*')
                """
                if col1[g] == col2[g]:
                    print(col1[g])
                    print('Coincidencia Columna' + str(col2[g]))
                    new_m.insertar(j, int(col1[g]), '*')
                """
            except:
                continue
        except:
            continue

    lista_matrices.AgregarFinal(new_m)
    Grafo1(nombre)

    reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
        time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
        time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
        nom_mat) + ', ' + str(nom_mat_1) + ' - Operacion: ' + 'Interseccion')

def Diferencia():
    jojos()
    nom_mat = cajaMatriz.get()
    nom_mat_1 = cajaM2.get()
    try:
        Datos1 = lista_matrices.Listar(nom_mat).devolverFilas()
        Datos2 = lista_matrices.Listar(nom_mat_1).devolverFilas()

        Grafo(nom_mat)
        Grafo2(nom_mat_1)
    except:
        reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
            time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
            time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Error: Matriz Inexistente')
        return
    nombre = 'Matriz_D'
    fil = int(lista_matrices.Listar(nom_mat).filas)
    col = int(lista_matrices.Listar(nom_mat).columnas)
    new_m = Ortogonal(str(nombre), int(fil), int(col))

    for v in Datos1:
        for b in Datos1[v]:
            try:
                coincidencia = Datos2[v]
                if b in coincidencia:
                    continue
                else:
                    new_m.insertar(v, b, '*')
            except:
                new_m.insertar(v, b, '*')
    """
    for e in Datos2:
        for c in Datos2[e]:
            if e > int(fil) or c > int(col):
                reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
                    time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
                    time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
                    nom_mat) + ', ' + str(nom_mat_1) + ' - Error: ' + 'Nodos fuera de index')
                return
            else:
                new_m.Borrar_Nodo(e, c)
    """

    lista_matrices.AgregarFinal(new_m)
    Grafo1(nombre)

    reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
        time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
        time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
        nom_mat) + ', ' + str(nom_mat_1) + ' - Operacion: ' + 'Diferencia')

def Diferencia1():
    jojos()
    Diferencia()
    nom_mat_1 = cajaMatriz.get()
    nom_mat = cajaM2.get()
    try:
        Datos1 = lista_matrices.Listar(nom_mat).devolverFilas()
        Datos2 = lista_matrices.Listar(nom_mat_1).devolverFilas()

        Grafo(nom_mat)
        Grafo2(nom_mat_1)
    except:
        reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
            time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
            time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Error: Matriz Inexistente')
        return
    nombre = 'Matriz_D1'
    fil = lista_matrices.Listar(nom_mat).filas
    col = lista_matrices.Listar(nom_mat).columnas
    new_m = Ortogonal(str(nombre), int(fil), int(col))

    for v in Datos1:
        for b in Datos1[v]:
            try:
                coincidencia = Datos2[v]
                if b in coincidencia:
                    continue
                else:
                    new_m.insertar(v, b, '*')
            except:
                new_m.insertar(v, b, '*')

    """
    for v in Datos1:
        for b in Datos1[v]:
            new_m.insertar(v, b, '*')

    for e in Datos2:
        for c in Datos2[e]:
            if e > int(fil) or c > int(col):
                reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
                    time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
                    time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
                    nom_mat) + ', ' + str(nom_mat_1) + ' - Error: ' + 'Nodos fuera de index')
                return
            else:
                new_m.Borrar_Nodo(e, c)
    """

    lista_matrices.AgregarFinal(new_m)
    Grafo1(nombre)

    reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
        time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
        time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
        nom_mat) + ', ' + str(nom_mat_1) + ' - Operacion: ' + 'Diferencia')

def DiferenciaS():
    jojos()
    nom_mat = cajaMatriz.get()
    nom_mat_1 = cajaM2.get()
    try:
        Datos1 = lista_matrices.Listar(nom_mat).devolverFilas()
        Datos2 = lista_matrices.Listar(nom_mat_1).devolverFilas()
    except:
        reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
            time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
            time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Error: Matriz Inexistente')
        return

    Diferencia1()
    Union1()

    Grafo(nom_mat)
    Grafo2(nom_mat_1)

    reporte.append(str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(
        time.localtime().tm_year) + ' - ' + str(time.localtime().tm_hour) + ':' + str(
        time.localtime().tm_min) + ':' + str(time.localtime().tm_sec) + ' - Matrices: ' + str(
        nom_mat) + ', ' + str(nom_mat_1) + ' - Operacion: ' + 'Diferencia Simetrica')

menuBar = Menu(ventana)

ventana.config(menu=menuBar)

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
operaciones.add_command(label="Union", font="Helvetica 15", command=Union)
operaciones.add_command(label="Interseccion", font="Helvetica 15", command=Interseccion)
operaciones.add_command(label="Diferencia", font="Helvetica 15", command=Diferencia)
operaciones.add_command(label="Diferencia Simetrica", font="Helvetica 15", command=DiferenciaS)
operaciones.add_separator()
operaciones.add_command(label="Graficar", font="Helvetica 15", command=GraficarOriginal)
operaciones.add_command(label="Eliminar", font="Helvetica 15", command=BorrarUnNodo)

repo = Menu(menuBar, tearoff=0)
repo.add_command(label="HTML", font="Helvetica 15", command=GenerarReporte)

ayuda = Menu(menuBar, tearoff=0)
ayuda.add_command(label="Documentacion", font="Helvetica 15", command=Documentacion)
ayuda.add_command(label="Estudiante", font="Helvetica 15", command=DatosMi)

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
place_holder_3 = Label(ventana, bg="gray", width=48, height=28)
place_holder_3.place(x=800, y=100)

ventana.mainloop()
