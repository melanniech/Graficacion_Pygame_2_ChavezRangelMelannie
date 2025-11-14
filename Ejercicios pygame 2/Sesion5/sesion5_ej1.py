import pygame
import sys

# 1. Inicializar Pygame
pygame.init()

# 2. Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sesión 5 - Ejercicio 1: Ajuste de tamaño")

# 3. Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# 4. Cargar la imagendir
try:
    imagen_original = pygame.image.load("imagen.png")
except FileNotFoundError:
    print("Error: No se encontró el archivo 'imagen.png'")
    print("Por favor, descarga una imagen y guárdala como 'imagen.png' en la misma carpeta.")
    pygame.quit()
    sys.exit()

# Guardamos las dimensiones originales
ancho_original, alto_original = imagen_original.get_size()

# 5. Variables de estado
escala = 1.0  # La escala inicial es 100%
imagen_mostrada = imagen_original # Al inicio, la imagen mostrada es la original
pos_x = ANCHO // 2
pos_y = ALTO // 2

# 6. Reloj
reloj = pygame.time.Clock()

# Bucle principal del juego
ejecutando = True
while ejecutando:
    # 7. Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
            
        if evento.type == pygame.KEYDOWN:
            # Tecla + (aumentar tamaño)
            if evento.key == pygame.K_PLUS or evento.key == pygame.K_KP_PLUS:
                escala += 0.1
                
            # Tecla - (disminuir tamaño)
            if evento.key == pygame.K_MINUS or evento.key == pygame.K_KP_MINUS:
                escala -= 0.1
                # Evitar que la escala sea negativa o cero
                if escala < 0.1:
                    escala = 0.1
            
            # --- Actualizar la imagen ---
            # Calcular las nuevas dimensiones
            nuevo_ancho = int(ancho_original * escala)
            nuevo_alto = int(alto_original * escala)
            
            # Re-escalar la imagen *original* (esto evita distorsión)
            imagen_mostrada = pygame.transform.scale(imagen_original, (nuevo_ancho, nuevo_alto))


    # 8. Dibujar
    pantalla.fill(NEGRO) # Limpia la pantalla
    
    # Para centrar la imagen, obtenemos su rectángulo
    rect_imagen = imagen_mostrada.get_rect()
    rect_imagen.center = (pos_x, pos_y) # Centrarla en (pos_x, pos_y)
    
    pantalla.blit(imagen_mostrada, rect_imagen)


    # 9. Actualizar la pantalla
    pygame.display.flip()

    # 10. Limitar a 60 FPS
    reloj.tick(60)


# 11. Salir de Pygame
pygame.quit()
sys.exit()