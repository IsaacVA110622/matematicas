class rectangulo:
    def __init__(self, base, altura ):
        self.base=base
        self.altura=altura

    def  area(self):
        print(f"la altura es {self.base*self.altura}")


    def  perimetro(self):
        print(f'el perimetro es {self.altura*2+self.base*2}') 

rec01=rectangulo(4,5) 
rec01.area()

#rec02=rectangulo(20,10)
rec01.perimetro()