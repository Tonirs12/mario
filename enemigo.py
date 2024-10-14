class Enemigo: 
    def __init__(self,posicionx,posiciony,esIzquierda):
        self.posicionx=posicionx
        self.posiciony=posiciony
        self.imagen=(0,2,136,12,15)
        self.velocidadx=1
        self.velocidady=-3
        self.enemigoSalta=False
        self.esIzquierda=esIzquierda

    def moverse(self,plataformas,suelos):

        if self.posicionx==0:
            self.esIzquierda=False
        elif self.posicionx==(266-15):
            self.esIzquierda=True


        if self.esIzquierda and self.posicionx>0:
            self.posicionx-=self.velocidadx 
            
        elif self.esIzquierda==False and self.posicionx<(266-15):
            self.posicionx+=self.velocidadx 
       
        if self.enemigoSalta==False:
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
                self.enemigoSalta=True
                self.velocidady=-3
    
    
    def actualizar(self,suelo,plataformas):
        self.moverse(plataformas,suelo)
        if self.enemigoSalta==True:
            self.posiciony-=self.velocidady
            
            if self.velocidady<0:

                for plataforma in plataformas:
                    filtroPlataformaY=plataforma.posiciony==self.posiciony+self.imagen[4] or (self.posiciony+self.imagen[4]+self.velocidady<plataforma.posiciony+plataforma.imagen[4] and self.posiciony+self.imagen[4]+self.velocidady>plataforma.posiciony)
                    filtroPlataformaX=plataforma.posicionx<=self.posicionx+self.imagen[3] and plataforma.posicionx+plataforma.imagen[3]>=self.posicionx
                    if (filtroPlataformaX and filtroPlataformaY):
                        self.enemigoSalta=False 
                        self.velocidady=0
                        self.posiciony=plataforma.posiciony-self.imagen[4]

                for bloque in suelo:
                    filtroBloqueY=bloque.posiciony==self.posiciony+self.imagen[4] or (self.posiciony+self.imagen[4]+self.velocidady<bloque.posiciony+bloque.imagen[4] and self.posiciony+self.imagen[4]+self.velocidady>bloque.posiciony)
                    filtroBloqueX=bloque.posicionx<=self.posicionx+self.imagen[3] and bloque.posicionx+bloque.imagen[3]>=self.posicionx
                    if (filtroBloqueX and filtroBloqueY):
                        self.enemigoSalta=False 
                        self.velocidady=0
                        self.posiciony=bloque.posiciony-self.imagen[4] 