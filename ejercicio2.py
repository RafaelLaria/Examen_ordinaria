class Numero:
    def __init__(self):
        self.numero = 0

    def __str__(self):
        return f'Numero: {self.numero}'
    
    def dar_numero(self):
        self.numero = int(input('Escriba el número: '))
    
    def suma_digitos(self, n = None):
        if n is None:
            self.numero = n
        if n < 10:
            return n
        else:
            return n%10 + self.suma_digitos(n//10)
        
num = Numero()
num.dar_numero()
num.suma_digitos()


            
