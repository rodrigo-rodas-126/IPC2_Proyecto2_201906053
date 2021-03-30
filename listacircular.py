from nodos import NodoGuardar
from matriz import Ortogonal

class NodoString:
  def __init__(self, linked_list=None, next=None):
    self.linked_list = linked_list
    self.next = next

class linked_list1:
  def __init__(self):
      self.head = None
      self.size = 0

  def insertar(self, linked_list):
      if not self.head:
          self.head = NodoString(linked_list=linked_list)
          return
      current = self.head
      while current.next:
          current = current.next
      current.next = NodoString(linked_list=linked_list)
      self.size += 1

  def imprimir(self):
      nodo = self.head
      while nodo != None:
          print(nodo.linked_list.string())
          nodo = nodo.next

  def eliminar_lista(self, linked_list):
      current = self.head
      previous = None

      while current and current.linked_list != linked_list:
          previous = current
          current = current.next
      if previous is None:
          self.head = current.next
      elif current:
          previous.next = current.next
          current.next = None

  def string(self):
      lista_cadena = '['
      nodo = self.head
      while nodo != None:
          if nodo.next is None:
              lista_cadena += str(nodo.linked_list.string())
          else:
              lista_cadena += str(nodo.linked_list.string())+','
          nodo = nodo.next
      lista_cadena += ']'
      print(lista_cadena)

  def devolver_tamano(self):
      if self.head is None:
          return
      else:
          return self.size+1

  def buscar_indice(self, indice):
      current = self.head
      if indice == 0:
          return current.linked_list
      else:
          if indice > self.size:
              return
          else:
              for num in range(indice):
                  if current.next == None:
                      return current.linked_list
                  else:
                      current = current.next
              return current.linked_list

  def borrar(self):
      self.head = None


class ListaCiruclar():

  def __init__(self):
    self.first = None
    self.last = None
    self.size = 0

  def Vacia(self):
    return self.first == None

  def AgregarInicio(self, Ortogonal):
    if self.Vacia():
      self.first = self.last = NodoGuardar(Ortogonal)
      self.last.next = self.first
    else:
      aux = NodoGuardar(Ortogonal)
      aux.next = self.first
      self.first = aux
      self.last.next = self.first
    self.size += 1

  def AgregarFinal(self, Ortogonal):
    if self.Vacia():
      self.first = self.last = NodoGuardar(Ortogonal)
      self.last.next = self.first
    else:
      aux = self.last
      self.last = aux.next = NodoGuardar(Ortogonal)
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
        print(aux.Ortogonal.nombre)
        aux = aux.next
      print(aux.Ortogonal.nombre)

  def Recorrer_String(self):
    nombres = []
    if self.Vacia():
      return
    else:
      aux = self.first
      while aux.next != self.first:
        nombres.append(aux.Ortogonal.nombre)
        aux = aux.next
      nombres.append(aux.Ortogonal.nombre)
      return nombres

  def Listar(self, nom_matr):
    cont_maz = -1
    aux = self.first
    aux1 = None
    if aux.Ortogonal.nombre == nom_matr:
      return self.first.Ortogonal
    else:
      while aux.next.Ortogonal.nombre != nom_matr:
        #print(cont_maz)
        cont_maz += 1
        #print(aux.dato)
        #aux1 = aux
        if cont_maz > self.tamano():
          return
        else:
          aux = aux.next
      return aux.next.Ortogonal


  def borra(self):
    self.first = self.last = None
