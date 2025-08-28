class CuentaBancaria:
    def __init__(self,titular,saldo:float):
        self.titular=titular
        self._saldo=saldo
    
    def depositar(self,cantidad):
        if cantidad<0:
            print("No se puede depositar números negativos")
        else:
            self._saldo+=cantidad
            print("Deposito Exitoso")
    
    def retirar(self,cantidad):
        if cantidad<0:
            print("!Error¡ No se puede retirar números negativos. ")
            return False
        elif cantidad>self._saldo:
            print("No se puede modificar el saldo")
            return False
        else:
            self._saldo-=cantidad
            print("Retiro Exitoso")
            return True
            

cuenta = CuentaBancaria("Maria", 300)
print("Titular:", cuenta.titular)
print("Saldo inicial:", cuenta._saldo)
cuenta.retirar(-400)
cuenta.retirar(100)   
cuenta.depositar(200)
cuenta.depositar(-200)