import pygame
import sys

# 1. Inicializar Pygame
pygame.init()

# 2. Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sesión 4 - Ejercicio 2: Pulsación")

# 3. Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# 4. Variables del círculo
# El radio inicial será de 20
radio = 20
# Qué tan rápido cambia el radio (0.5 píxeles por fotograma para un efecto suave)
velocidad_radio = 0.5

# Límites del radio
RADIO_MIN = 20
RADIO_MAX = 50

# Posición (lo dejaremos en el centro)
circulo_x = ANCHO // 2
circulo_y = ALTO // 2

# 5. Reloj
reloj = pygame.time.Clock()

# Bucle principal del juego
ejecutando = True
while ejecutando:
    # 6. Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # --- Lógica de crecimiento/encogimiento ---
    
    # 1. Actualizar el radio
    radio += velocidad_radio
    
    # 2. Comprobar los límites y revertir la dirección
    # Si el radio supera el máximo (50) o baja del mínimo (20)
    if radio > RADIO_MAX or radio < RADIO_MIN:
        # Invertimos la velocidad (si estaba en 0.5, ahora es -0.5, y viceversa)
        velocidad_radio = -velocidad_radio
    

    # 7. Dibujar
    pantalla.fill(NEGRO) # Limpia la pantalla
    
    # Dibujamos el círculo con el radio actual (convertido a entero)
    pygame.draw.circle(pantalla, BLANCO, (circulo_x, circulo_y), int(radio))


    # 8. Actualizar la pantalla
    pygame.display.flip()

    # 9. Limitar a 60 FPS
    reloj.tick(60)


# 10. Salir de Pygame
pygame.quit()
sys.exit()