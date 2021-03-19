class node:
  def __init__(self, cadena=None, next=None):
    self.cadena = cadena
    self.next = next

class linked_list:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertar(self, cadena):
        if not self.head:
            self.head = node(cadena=cadena)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node(cadena=cadena)
        self.size += 1

    def devolver_tamano(self):
        if self.head is None:
            return
        else:
            return self.size

    def imprimir(self):
        node = self.head
        while node is not None:
            if node.numero == None:
                return
            else:
                print(node.numero)
                node = node.next

    def string(self):
        lista_cadena = '['
        node = self.head
        while node != None:
            if node.next is None:
                lista_cadena += str(node.cadena)
            else:
                lista_cadena += str(node.cadena)+','
            node = node.next
        lista_cadena += ']'
        return lista_cadena

    def eliminar(self, cadena):
        current = self.head
        previous = None

        while current and current.numero != cadena:
            previous = current
            current = current.next
        if previous is None:
            self.head = current.next
        elif current:
            previous.next = current.next
            current.next = None

    def buscar_num(self, cadena):
        current = self.head
        previous = None

        while current and current.numero != cadena:
            previous = current
            current = current.next
        if current and current.numero == cadena:
            return True
        else:
            return False

    def devolver_tamano1(self):
        if self.head is None:
            return
        else:
            return self.size+1

    def buscar_indice(self, indice):
        current = self.head
        if indice == 0:
            return current.cadena
        else:
            if indice > self.size:
                return
            else:
                for num in range(indice):
                    if current.next == None:
                        return current.cadena
                    else:
                        current = current.next
                return current.cadena

    def borrar(self):
        self.head = None
        #self.head.next = None

class nodo:
  def __init__(self, linked_list=None, next=None):
    self.linked_list = linked_list
    self.next = next

class linked_list1:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertar(self, linked_list):
        if not self.head:
            self.head = nodo(linked_list = linked_list)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = nodo(linked_list=linked_list)
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