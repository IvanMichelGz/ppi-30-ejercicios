class Operacion:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def suma(self):
        suma=(self.x)+(self.y)
        return suma
    
    def multiplicacion(self):
        multi=(self.x)*(self.y)
        return multi
    
    def division(self):
        if  self.y==0:
            print("¡Divisón de x por y es imposible!")
        else:
            divi=(self.x)/(self.y)
            return divi


operacion1=Operacion(3,2)
print(f"La suma es {operacion1.suma()}")
print(f"La multiplicación es: {operacion1.multiplicacion()}")
print(f"La división es: {operacion1.division()}")
operacion1.y=0
operacion1.division()

