from nodo import Nodo
from ortogonal import *

class ListaCiruclar():

  def __init__(self):
    self.first = None
    self.last = None
    self.size = 0

  def Vacia(self):
    return self.first == None

  def AgregarInicio(self, Matriz):
    if self.Vacia():
      self.first = self.last = Nodo(Matriz)
      self.last.next = self.first
    else:
      aux = Nodo(Matriz)
      aux.next = self.first
      self.first = aux
      self.last.next = self.first
    self.size += 1

  def AgregarFinal(self, Matriz):
    if self.Vacia():
      self.first = self.last = Nodo(Matriz)
      self.last.next = self.first
    else:
      aux = self.last
      self.last = aux.next = Nodo(Matriz)
      self.last.next = self.first
    self.size += 1

  def tamano(self):
    if self.Vacia():
      return
    else:
      return self.size

  def Recorrer(self):
    if self.Vacia():
      return
    else:
      aux = self.first
      while aux.next != self.first:
        print(aux.Matriz.nombre)
        aux = aux.next
      print(aux.Matriz.nombre)

  def Recorrer_String(self):
    nombres = linked_list1()
    if self.Vacia():
      return
    else:
      aux = self.first
      while aux.next != self.first:
        nombres.insertar(aux.Matriz.nombre)
        aux = aux.next
      nombres.insertar(aux.Matriz.nombre)
      return nombres

  def Listar(self, nom_matr):
    cont_maz = -1
    aux = self.first
    aux1 = None
    if aux.Matriz.nombre == nom_matr:
      return self.first.Matriz
    else:
      while aux.next.Matriz.nombre != nom_matr:
        #print(cont_maz)
        cont_maz += 1
        #print(aux.dato)
        #aux1 = aux
        if cont_maz > self.tamano():
          return
        else:
          aux = aux.next
      return aux.next.Matriz


  def borra(self):
    self.first = self.last = None
