class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def Calcular_Area(self):
        print(f"Calculando el área del {self.nombre}")


class Circulo(FiguraGeometrica):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio
        
    def Calcular_Area(self):
        super().Calcular_Area()
        area = 3.1416 * (self.radio ** 2)
        return area

class Rectangulo(FiguraGeometrica):
    def __init__(self, nombre,lado,ancho):
        super().__init__(nombre)
        self.lado=lado
        self.ancho=ancho    
    def Calcular_Area(self):
        super().Calcular_Area()
        area=self.lado*self.ancho
        return area

class Triangulo(FiguraGeometrica):
    def __init__(self, nombre,ancho, altura):
        super().__init__(nombre)
        self.altura=altura
        self.ancho=ancho
    def Calcular_Area(self):
        super().Calcular_Area()
        area=self.altura*self.ancho*0.5
        return area

figura1 = Circulo("círculo", 5)
print(f"Área {figura1.nombre}: {figura1.Calcular_Area()}")
figura2= Rectangulo("Rectangulo",5,4)
print(f"Área {figura2.nombre}: {figura2.Calcular_Area()}")
figura3=Triangulo("Triangulo",4,3)
print(f"Área {figura3.nombre}: {figura3.Calcular_Area()}")