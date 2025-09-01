class Paleta:
    def __init__(self,sabor:str,precio):
        self.sabor=sabor
        self.precio=float(precio)
    
    def mostrarInformación(self):
        print(f"El sabor de la paleta es: {self.sabor}")
        print(f"El Precio de la paleta es: {self.precio}")
    
    def cambiarPrecio():
        pass
        
class PaletaAgua(Paleta):
    def __init__(self, sabor, precio, baseAgua:bool):
        super().__init__(sabor, precio)
        self.baseAgua=baseAgua
    
    def mostrarBaseAgua(self):
        if self.baseAgua:
            print("Tu paleta tiene base de agua")
        else:
            print("Tu paleta no tiene base de agua")
    
    def cambiarPrecio(self):
        self.precio+=2
            
class PaletaCrema(Paleta):
    def __init__(self, sabor, precio, cremosa:bool):
        super().__init__(sabor, precio)
        self.cremosa=cremosa
    
    def mostrarTexturaCremosa(self):
        if self.cremosa:
            print("Tu paleta es cremosa")
        else:
            print("No es cremosa")
    
    def cambiarPrecio(self):
        self.precio+=6

p1 = PaletaAgua("Limón", 10,True)
p2 = PaletaCrema("Chocolate", 12,False)

p1.cambiarPrecio()  # +2
p2.cambiarPrecio()  # +6

p1.mostrarInformación() 
p2.mostrarInformación()  

p1.mostrarBaseAgua()
p2.mostrarTexturaCremosa()