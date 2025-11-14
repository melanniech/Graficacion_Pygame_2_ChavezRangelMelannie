import pygame
import sys

# 1. Inicializar Pygame
pygame.init()

# 2. Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sesión 4 - Ejercicio 3: Gravedad")

# 3. Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
SUELO_COLOR = (70, 70, 70) # Un color gris para el "suelo"

# 4. Variables de la pelota
radio = 25
# Posición inicial (arriba a la izquierda)
circulo_x = 100
circulo_y = 50

# 5. Variables de física
velocidad_y = 0  # Empieza sin velocidad vertical
gravedad = 0.5   # La aceleración
# El rebote pierde 20% de energía, así que conserva el 80% (0.8)
factor_rebote = 0.8 

# 6. Reloj
reloj = pygame.time.Clock()

# Bucle principal del juego
ejecutando = True
while ejecutando:
    # 7. Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # --- Lógica de Gravedad y Rebote ---
    
    # 1. Aplicar la gravedad a la velocidad
    # En cada fotograma, la velocidad_y aumenta debido a la gravedad
    velocidad_y += gravedad
    
    # 2. Mover la pelota
    circulo_y += velocidad_y
    
    # 3. Comprobar colisión con el suelo
    # Si la parte de abajo de la pelota (circulo_y + radio) supera el ALTO
    if circulo_y + radio > ALTO:
        # Colocamos la pelota justo en el suelo para evitar que se "hunda"
        circulo_y = ALTO - radio
        
        # Invertimos la velocidad
        velocidad_y = -velocidad_y
        
        # Aplicamos la pérdida de energía (reducimos la velocidad del rebote)
        velocidad_y *= factor_rebote

    # 8. Dibujar
    pantalla.fill(NEGRO) # Limpia la pantalla
    
    # Dibujamos la pelota
    pygame.draw.circle(pantalla, BLANCO, (int(circulo_x), int(circulo_y)), radio)


    # 9. Actualizar la pantalla
    pygame.display.flip()

    # 10. Limitar a 60 FPS
    reloj.tick(60)


# 11. Salir de Pygame
pygame.quit()
sys.exit()