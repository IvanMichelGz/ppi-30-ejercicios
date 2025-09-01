class Personaje:
    def __init__(self,nombre,nivel):
        self.nombre=nombre
        self.nivel=nivel

    def atacar(self):
        print(f"{self.nombre}Ataca un golpe crítico")
        
class Jugador(Personaje):
    def __init__(self, nombre, nivel, clase):
        super().__init__(nombre, nivel)
        self.clase=clase
    
    def usarHabilidadEspecial(self):
        print(f"{self.nombre} realizo una habilidad especial")
        
class Enemigo(Personaje):
    def __init__(self, nombre, nivel, tipo):
        super().__init__(nombre, nivel)
        self.tipo=tipo
    def gritar(self):
        print(f"{self.nombre} grita: Aaaaah (El ataque le hizo mucho daño)")

j1 = Jugador("Arthas", 10, "Paladín")
e1 = Enemigo("Orco", 5, "Guerrero")

j1.atacar()
j1.usarHabilidadEspecial()

e1.atacar()
e1.gritar()
