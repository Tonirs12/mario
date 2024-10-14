from vida import Vidas
IMAGENCAMINANDO=(0,17,1,15,23)
IMAGENPARADO=(0,0,0,15,23)
IMAGENSALTANDO=(0,65,0,15,23)
class Mario:
    def __init__(self,posicionx,posiciony):
        self.posicionx=posicionx
        self.posiciony=posiciony
        self.marioSalta=False
        self.imagen=IMAGENPARADO
        self.velocidadx=3
        self.velocidady=3
        self.capacidadDeSalto=50
        self.posicionSalto=posiciony
        self.vidas=self.crearVidas()

        self.contador=5
    

    def moverse(self,esIzquierda,plataformas,suelos):
        self.imagen=IMAGENCAMINANDO
        if esIzquierda and self.posicionx>0:
            self.posicionx-=self.velocidadx 
            
        elif esIzquierda==False and self.posicionx<(266-15):
            self.posicionx+=self.velocidadx 
       
        if self.marioSalta==False:
            platafromaEncontrada=False
            for plataforma in plataformas:
                filtroPlataformaY=self.posiciony==plataforma.posiciony-self.imagen[4]
                filtroPlataformaX=(plataforma.posicionx<=self.posicionx+self.imagen[3] and plataforma.posicionx+plataforma.imagen[3]>=self.posicionx)
                if (filtroPlataformaX and filtroPlataformaY):
                    platafromaEncontrada=True

            for bloque in suelos:
                filtrobloqueY=self.posiciony==bloque.posiciony-self.imagen[4]
                filtrobloqueX=(bloque.posicionx<=self.posicionx+self.imagen[3] and bloque.posicionx+bloque.imagen[3]>=self.posicionx)
                if (filtrobloqueX and filtrobloqueY):
                    platafromaEncontrada=True
            if platafromaEncontrada==False:
                self.marioSalta=True
                self.velocidady=-3
       
    def pararse(self):
        if self.contador>0:
            self.contador-=1
        elif self.marioSalta==False or (self.marioSalta==True and self.velocidady==-3):
            self.imagen=IMAGENPARADO
            self.contador=5
    
    def saltar(self):
        if self.marioSalta==False:
            self.imagen=IMAGENSALTANDO
            self.marioSalta=True
            self.velocidady=3
            self.posicionSalto=self.posiciony
        
    def actualizar(self,suelo,plataformas):
        if self.marioSalta==True:
            self.posiciony-=self.velocidady
            # posicion salto, capacidad salto, resultado es hasta donde salta 
            # posiciony,velocidad
            nivelDeSalto = self.posicionSalto-self.capacidadDeSalto
            if (self.posiciony-nivelDeSalto)>30:
               self.velocidady=3 if self.velocidady>0 else -3
            elif (self.posiciony-nivelDeSalto)>10:
                self.velocidady=2 if self.velocidady>0 else -2
            else:
                self.velocidady=1 if self.velocidady>0 else -1
            if nivelDeSalto==self.posiciony:
                self.velocidady*=-1
            if self.velocidady<0:

                for plataforma in plataformas:
                    filtroPlataformaY=plataforma.posiciony==self.posiciony+self.imagen[4] or (self.posiciony+self.imagen[4]+self.velocidady<plataforma.posiciony+plataforma.imagen[4] and self.posiciony+self.imagen[4]+self.velocidady>plataforma.posiciony)
                    filtroPlataformaX=plataforma.posicionx<=self.posicionx+self.imagen[3] and plataforma.posicionx+plataforma.imagen[3]>=self.posicionx
                    if (filtroPlataformaX and filtroPlataformaY):
                        self.marioSalta=False 
                        self.velocidady=0
                        self.posiciony=plataforma.posiciony-self.imagen[4]

                for bloque in suelo:
                    filtroBloqueY=bloque.posiciony==self.posiciony+self.imagen[4] or (self.posiciony+self.imagen[4]+self.velocidady<bloque.posiciony+bloque.imagen[4] and self.posiciony+self.imagen[4]+self.velocidady>bloque.posiciony)
                    filtroBloqueX=bloque.posicionx<=self.posicionx+self.imagen[3] and bloque.posicionx+bloque.imagen[3]>=self.posicionx
                    if (filtroBloqueX and filtroBloqueY):
                        self.marioSalta=False 
                        self.velocidady=0
                        self.posiciony=bloque.posiciony-self.imagen[4]
            
            elif self.velocidady>0:

                for plataforma in plataformas:
                    filtroPlataformaY=plataforma.posiciony+plataforma.imagen[4]==self.posiciony or (self.posiciony+self.velocidady<plataforma.posiciony and self.posiciony+self.velocidady>plataforma.posiciony+plataforma.imagen[4])

                    filtroPlataformaX=plataforma.posicionx<=self.posicionx+self.imagen[3] and plataforma.posicionx+plataforma.imagen[3]>=self.posicionx
                    if (filtroPlataformaX and filtroPlataformaY):
                        if self.velocidady>0:
                            self.velocidady*=-1
                        



    def crearVidas(self):
        return [Vidas(10,10,8,6),Vidas(20,10,8,6),Vidas(30,10,8,6)]
    
