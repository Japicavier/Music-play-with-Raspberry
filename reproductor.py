import pygame 
# from importa solo secciones de la bilbioteca
from pygame.locals import *
from time import sleep
from gpiozero import *

canciones=["musica/imagine-dragons-follow-you.mp3","musica/joji-run-lyrics.mp3","musica/todo-de-ti.mp3"]
imagenes=["Fondos/folow-you-imagine-dragons.jpg","Fondos/run-joji.jpg","Fondos/todo-de-ti.png"]

pause_continue_btn = Button(27)
next_btn = Button(26)
rewind_btn = Button(25)
StopLED = LED(4)

indice=0;

pygame.init()
width = 600
height = 450

while(1):
    if(indice==3):
        indice=0
    pygame.mixer.music.load(canciones[indice])
    pygame.mixer.music.play()
    
    while(pygame.mixer.music.get_busy()):
        if(rewind_btn.is_pressed):
            sleep(0.3)
            pygame.mixer.music.play()
        if(next_btn.is_pressed):
            sleep(0.3)
            break
        if(pause_continue_btn.is_pressed):
            sleep(0.3)
            StopLED.on()
            pygame.mixer.music.pause()
            pause_continue_btn.wait_for_press()
            sleep(0.3)
            StopLED.off()
            pygame.mixer.music.unpause()
        screen = pygame.display.set_mode((width, height))
        # Mostrar la imagen
        foto = pygame.image.load(imagenes[indice])
        # Maximizar la imagen en la pantalla
        foto = pygame.transform.scale(foto, (width, height))
        screen.blit(foto, (0, 0))
        # blitting o transferencia de bloques de bits
        pygame.display.update()
        sleep(0.01)
    indice+=1
