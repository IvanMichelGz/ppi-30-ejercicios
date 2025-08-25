class Persona:
    def __init__(self,nombre,edad,genero):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
    
    def presentarse(self):
        print(f"Mi nombre es {self.nombre}, tnego {self.edad} años y soy un {self.genero}")
    
    def esAdulto(self):
        if self.edad>=18:
            return print("True")
        else:
            return print("False")

persona1=Persona("martin",23,"hombre")
persona1.presentarse()
persona1.esAdulto()