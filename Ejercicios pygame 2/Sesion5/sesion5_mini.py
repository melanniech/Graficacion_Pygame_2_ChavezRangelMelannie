import pygame
import sys
import math

# 1. Inicializar Pygame
pygame.init()

# 2. Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sesión 5 - Mini-proyecto: Nave")

# 3. Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# 4. Cargar la imagen de la nave
try:
    # Carga la nave que descargaste y renombraste
    # Usamos .convert_alpha() por si tiene transparencias
    nave_original = pygame.image.load("nave.png").convert_alpha()
except FileNotFoundError:
    print("Error: No se encontró el archivo 'nave.png'")
    print("Por favor, descarga 'ship_0001.png' de OpenGameArt,")
    print("renómbralo a 'nave.png' y guárdalo en la carpeta.")
    pygame.quit()
    sys.exit()

# 5. Escalar la nave
# La imagen original es pequeña, la escalamos a un tamaño razonable
# (El ejercicio pide usar pygame.transform.scale)
ANCHO_NAVE, ALTO_NAVE = 64, 64
nave_original = pygame.transform.scale(nave_original, (ANCHO_NAVE, ALTO_NAVE))

# 6. Variables de la nave
# Usamos Vectores (facilitan las matemáticas)
# pygame.math.Vector2 es un par de (x, y)
posicion_nave = pygame.math.Vector2(ANCHO // 2, ALTO // 2)
velocidad = 0
angulo = 0
VELOCIDAD_MOVIMIENTO = 5
VELOCIDAD_ROTACION = 5 # Qué tan rápido gira

# 7. Reloj
reloj = pygame.time.Clock()

# Bucle principal del juego
ejecutando = True
while ejecutando:
    # 8. Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # --- Lógica del Juego ---

    # 1. Obtener teclas presionadas
    teclas = pygame.key.get_pressed()
    
    # 2. Obtener posición del ratón
    pos_raton = pygame.mouse.get_pos()

    # 3. Calcular el ángulo hacia el ratón
    # Restamos la posición del ratón y la de la nave para obtener un vector
    dx = pos_raton[0] - posicion_nave.x
    dy = pos_raton[1] - posicion_nave.y
    
    # Usamos atan2 para obtener el ángulo en radianes
    # Sumamos 90 grados (math.pi/2) porque la imagen 'nave.png' apunta hacia ARRIBA
    # Pygame (y las matemáticas) consideran 0 grados hacia la DERECHA
    # math.degrees() lo convierte de radianes a grados
    angulo_objetivo_rad = math.atan2(-dy, dx) 
    angulo_objetivo_grados = math.degrees(angulo_objetivo_rad) - 90

    # 4. Rotar la nave
    # ¡Importante! Siempre rotar desde la imagen *original*
    # Si rotas una imagen ya rotada, se degrada y se deforma
    angulo = angulo_objetivo_grados # Para este ejercicio, rotamos instantáneamente
    nave_rotada = pygame.transform.rotate(nave_original, angulo)
    
    # 5. Mover la nave
    velocidad = 0
    if teclas[pygame.K_w] or teclas[pygame.K_UP]:
        velocidad = VELOCIDAD_MOVIMIENTO

    # Calcular la dirección (hacia dónde se moverá)
    # Convertimos el ángulo de vuelta a radianes para usar sin y cos
    angulo_mov_rad = math.radians(-angulo - 90) # Ajuste por cómo Pygame maneja los ángulos
    vector_direccion = pygame.math.Vector2(math.cos(angulo_mov_rad), math.sin(angulo_mov_rad))
    
    posicion_nave += vector_direccion * velocidad


    # 9. Dibujar
    pantalla.fill(NEGRO) # Limpia la pantalla
    
    # Para dibujar la nave rotada centrada, obtenemos su nuevo 'rect'
    rect_nave = nave_rotada.get_rect(center=posicion_nave)
    
    pantalla.blit(nave_rotada, rect_nave)

    # 10. Actualizar la pantalla
    pygame.display.flip()

    # 11. Limitar a 60 FPS
    reloj.tick(60)


# 12. Salir de Pygame
pygame.quit()
sys.exit()