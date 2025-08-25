class Circulo:
    def __init__(self,x,y,R:float):
        self.x=x
        self.y=y
        self.R=R
    
    def area(self):
        area:float= ((self.R)**2)*(3.1416)
        return area
    
    def perimetro(self):
        perimetro:float=2*(self.R)*(3.1416)
        return perimetro
    
    def mostrar_propiedades(self):
        print(f"El círculo tiene un radio de {self.R} y su centro es O({self.x},{self.y})")

circulo_1=Circulo(3,4,5)
circulo_1.mostrar_propiedades()
print(f"El perímetro del circulo 1 es: {circulo_1.perimetro():.2f}")
print(f"El área del circulo 1 es: {circulo_1.area():.2f}")