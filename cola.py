class Cola:
  def __init__(self):
    self.cola = []

  def encolar(self, cadena):
    self.cola.append(cadena)

  def devolver_tamano(self):
    return len(self.cola)

  def imprimir(self):
    for cadena in self.cola:
      print(cadena, end="")

  def desencolar(self):
    if self.cola:
      ff = self.cola.pop(0)
      return ff