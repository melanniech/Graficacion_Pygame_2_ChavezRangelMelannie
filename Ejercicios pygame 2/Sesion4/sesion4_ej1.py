import pygame
import sys

# 1. Inicializar Pygame
pygame.init()

# 2. Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sesión 4 - Ejercicio 1: Rebote (Acelerado)")

# 3. Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# 4. Variables del círculo
radio = 25
# Posición inicial (en el centro)
circulo_x = ANCHO // 2
circulo_y = ALTO // 2
# Velocidad inicial
velocidad_x = 5.0  
velocidad_y = 5.0

# Crear un reloj para controlar los FPS
reloj = pygame.time.Clock()

# Bucle principal del juego
ejecutando = True
while ejecutando:
    # 5. Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # 6. Lógica de movimiento
    circulo_x += velocidad_x
    circulo_y += velocidad_y
    
    # Comprobar colisión con paredes (rebote)
    
    # Paredes izquierda o derecha
    if circulo_x + radio > ANCHO or circulo_x - radio < 0:
        velocidad_x = -velocidad_x  # Invertir dirección X
        
        # Incrementar la velocidad (magnitud) en 0.5
        if velocidad_x > 0:
            velocidad_x += 0.5 # <-- AUMENTADO
        else:
            velocidad_x -= 0.5 # <-- AUMENTADO

    # Paredes superior o inferior
    if circulo_y + radio > ALTO or circulo_y - radio < 0:
        velocidad_y = -velocidad_y  # Invertir dirección Y
        
        # Incrementar la velocidad (magnitud) en 0.5
        if velocidad_y > 0:
            velocidad_y += 0.5 # <-- AUMENTADO
        else:
            velocidad_y -= 0.5 # <-- AUMENTADO


    # 7. Dibujar
    pantalla.fill(NEGRO)  # Limpia la pantalla con color negro
    pygame.draw.circle(pantalla, BLANCO, (int(circulo_x), int(circulo_y)), radio)


    # 8. Actualizar la pantalla
    pygame.display.flip()

    # 9. Limitar a 60 FPS
    reloj.tick(60)


# 10. Salir de Pygame
pygame.quit()
sys.exit()