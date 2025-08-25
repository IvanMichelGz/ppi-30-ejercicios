import random
class Dado:
    def __init__(self, puntos=0):
        self.puntos=puntos
    
    def lanzar_dado(self):
        self.puntos=random.randint(1,6)
        return self.puntos
    
    def mostrar_puntos(self):
        print(f"El número de puntos obtenidos es: {self.puntos}")

lanzamiento_1=Dado()
lanzamiento_1.lanzar_dado()
lanzamiento_1.mostrar_puntos()