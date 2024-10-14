class Tuberia:
    def __init__(self,posicionx,posiciony,ancho,alto,derecha):
        self.posicionx=posicionx
        self.posiciony=posiciony
        self.ancho=ancho
        self.alto=alto
        self.imagen=(1,80,32,16,16)
        if derecha:
            self.imagen=(1,96,32,16,16)