class Estudiante:
    def __init__(self,nombre,edad,genero,nivel):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.nivel=nivel
    
    def inscripcion(self,estudiantes_inscritos):
        estudiante=self.nombre,self.edad,self.genero,self.nivel
        estudiantes_inscritos.append(estudiante)
        return estudiantes_inscritos


estudiante1=Estudiante("Fabrice",17,"hombre","segundo año")
estudiante2=Estudiante("Julie",8,"mujer","primaria")
print(f"Los estudiantes incritos en los curso: {estudiante1.inscripcion()},{estudiante2.inscripcion()
      }")           