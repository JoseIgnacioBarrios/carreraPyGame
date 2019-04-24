import pygame
import sys
class Game():
    corredores=[]
    
    def __init__(self):
        self.__screen=pygame.display.set_mode((640,480))
        pygame.display.set_caption("Carrera de Bichos")
        ##Direccion de la imagen
        self.background=pygame.image.load("imagenes/background.png")
        
       ## self.runner=pygame.image.load("imagenes/background.png")

    def competir(self):
        while True:
            #Comprobacion de los eventos
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            ##comando que Refresca/renderizar la pantalla
            self.__screen.blit(self.background,(0,0))
            pygame.dislay.flip()

if __name__ == '__main__':
    pygame.init()
    game=Game()