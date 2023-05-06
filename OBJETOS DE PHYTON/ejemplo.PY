#definicion del objeto
class pokemon:

    def __init__(self, especie, brazos, poderes, instrumentos):
        self.especies=especie
        self.brazo=brazos
        self.poderes=poderes
        self.instrumentos=instrumentos

    def evolucion(self, piedra, piedra2): 
        print(self.especie)
        if(self.esoecie=='electrico'):
            return 'evoluciona raichu'
        elif(piedra=='rayo'and piedra2=='agua'):
            return 'evoluciona nwtwo'
        else:
            return 'es un perro'
        
    def get(self):
        print(self.especie)

    def set( self,especie):
        self.especie=especie

#
pikachu=pokemon('agua',2,'velocidad','no tiene')
charamander=pokemon('fuego',2,'bola de fuego',"no tiene")






