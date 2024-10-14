from board import Tablero
import pyxel

tablero = Tablero(266, 266)
pyxel.init(tablero.ancho, tablero.alto, title = "This is Super Mario")


pyxel.load("ASSETS/mario.pyxres")
pyxel.run(tablero.actualizar, tablero.dibujar)


# Done
# ● Si se tarda demasiado tiempo en patear un enemigo volteado, este se levanta, aumenta la velocidad y cambia de color,
# ● Al golpear el bloque POW los enemigos que se encuentren tocando el suelo o una plataforma se dan la vuelta y quedan boca arriba, por lo que luego podremos patearlos.
# ● Implementar en este sprint las animaciones de Mario y de los enemigos.
# ● Cuando se hayan destruido todos los enemigos, el juego finaliza.
# ● Si Mario entra en contacto con un enemigo en movimiento, recibe daño y consumirá una vida. Si Mario pierde todas las vidas se acabará el juego.
# ● Si se patea un enemigo volteado, éste es destruido.

# ToDo
# ● Cuando se golpea una plataforma debajo de un enemigo, el enemigo reacciona según lo especificado para cada uno de los tipos, volteándose o desapareciendo. 
# ● Al obtener monedas aumentará el contador de monedas y la puntuación. Al destruir un enemigo aumentará también la puntuación.
# ● Mostrar y aumentar puntuación

# ● Implementar las distintas pantallas del juego.
# ● Implementar las distintas fases del juego
