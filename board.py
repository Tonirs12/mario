

import pyxel
from suelo import Suelo
from tuberia import Tuberia
from pow import Pow
from plataforma import Plataforma
from mario import Mario
from enemigo import Enemigo

# Le damos nombre al objeto que vamos a hacer
class Tablero:
    # Caracteristicas que queremos que tenga
    def __init__ (self,ancho,alto):
        self.ancho=ancho
        self.alto=alto
        self.suelo=[]
        self.tuberias=[]
        mitadxmapa=266/2 -16/2 
        self.pow=Pow(mitadxmapa,190,16,16)
        self.mario=Mario(mitadxmapa,206,)
        self.plataformas=[]
        self.enemigos=[]
        
        self.crearTuberias()

        self.crearSuelo()

        self.crearPlataformas()

        self.crearEnemigos()

      
    # Dibujar los objetos
    def dibujar(self):
        # Va a pintar toda la pantalla para que luego no se repitan
        pyxel.cls(0)
        for bloque in self.suelo:
            # Pinta el suelo
            pyxel.blt(bloque.posicionx,bloque.posiciony,bloque.imagen[0],bloque.imagen[1],bloque.imagen[2],bloque.imagen[3],bloque.imagen[4])
        # Recorre la lista  
        for tuberia in self.tuberias:
            # Pinta la tuberia
            pyxel.blt(tuberia.posicionx,tuberia.posiciony,tuberia.imagen[0],tuberia.imagen[1],tuberia.imagen[2],tuberia.imagen[3],tuberia.imagen[4])

        pyxel.blt(self.pow.posicionx,self.pow.posiciony,self.pow.imagen[0],self.pow.imagen[1],self.pow.imagen[2],self.pow.imagen[3],self.pow.imagen[4])

        for plataforma in self.plataformas:
            # Pinta laplataforma
            pyxel.blt(plataforma.posicionx,plataforma.posiciony,plataforma.imagen[0],plataforma.imagen[1],plataforma.imagen[2],plataforma.imagen[3],plataforma.imagen[4])   
        
        
        pyxel.blt(self.mario.posicionx,self.mario.posiciony,self.mario.imagen[0],self.mario.imagen[1],self.mario.imagen[2],self.mario.imagen[3],self.mario.imagen[4])
  
        for vida in self.mario.vidas:
            pyxel.blt(vida.posicionx,vida.posiciony,vida.imagen[0],vida.imagen[1],vida.imagen[2],vida.imagen[3],vida.imagen[4])
        
        for enemigo in self.enemigos:
            pyxel.blt(enemigo.posicionx,enemigo.posiciony,enemigo.imagen[0],enemigo.imagen[1],enemigo.imagen[2],enemigo.imagen[3],enemigo.imagen[4])

    # Va a actualizar el estado de nuestros objetos para que cuando pintemos se vea bien
    def actualizar(self):
        self.mario.pararse()
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.mario.moverse(True,self.plataformas,self.suelo)
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.mario.moverse(False,self.plataformas,self.suelo)
        elif pyxel.btnp(pyxel.KEY_UP):
            self.mario.saltar()
      
        self.mario.actualizar(self.suelo,self.plataformas)
        
        for enemigo in self.enemigos:
            enemigo.actualizar(self.suelo,self.plataformas)

    def crearTuberias(self):
        # creamos la tuberia
        tuberia1=Tuberia(0,211,16,16,False)
        # guardamos la tuberia
        self.tuberias.append(tuberia1)
        # Creamos la nueva tuberia
        tuberia2=Tuberia(0,55,16,16,False)
        # Guardamos la nueva tuberia
        self.tuberias.append(tuberia2)
        tuberia3=Tuberia(250,211,16,16,True)
        self.tuberias.append(tuberia3)
        tuberia4=Tuberia(250,55,16,16,True)
        self.tuberias.append(tuberia4)

    def crearSuelo(self):
        # Decimos donde empezamos
        posicionSueloX=0
        for i in range(0,266,16):       
            # Creamos el bloque
            bloque=Suelo(posicionSueloX,245,16,16)
            # Guardamos el bloque
            self.suelo.append(bloque)
            # Creamos otra vez el bloque
            nuevoBloque=Suelo(posicionSueloX,229,16,16)
            # Guardamos el nuevo bloque
            self.suelo.append(nuevoBloque)
            # Actualizamos donde empezamos con el ancho del bloque
            posicionSueloX+=16

    
    def crearPlataformas(self):
        posicionPlataformaX=0
        for i in range(0,266,19):
            if posicionPlataformaX<266/2 -19*2 or posicionPlataformaX >=266/2 +19*2:
                plataforma=Plataforma(posicionPlataformaX,190,19,7)
                self.plataformas.append(plataforma)
            if posicionPlataformaX<266/2 -19 or posicionPlataformaX >=266/2 +19:
                nuevaPlataforma=Plataforma(posicionPlataformaX,73,19,7)
                self.plataformas.append(nuevaPlataforma)
            if posicionPlataformaX <19*2 or posicionPlataformaX >=266-19*2:
                plataforma=Plataforma(posicionPlataformaX,151,19,7)
                self.plataformas.append(plataforma)
            else:       
                ultimaPlataforma=Plataforma(posicionPlataformaX,112,19,7)        
                self.plataformas.append(ultimaPlataforma)   
            posicionPlataformaX+=19 

    def crearEnemigos(self):
        enemigo=Enemigo(0,55,False)
        self.enemigos.append(enemigo)


     

