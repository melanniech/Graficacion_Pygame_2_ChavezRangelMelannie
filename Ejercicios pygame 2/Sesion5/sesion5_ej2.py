import pygame
import sys

# 1. Inicializar Pygame
pygame.init()

# 2. Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sesión 5 - Ejercicio 2: El Fantasma (6 Frames)")

# 3. Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
FONDO_OSCURO = (40, 40, 40) # Fondo oscuro para el fantasma

# 4. Cargar la hoja de sprites
try:
    # Carga el nuevo archivo "fantasma.png"
    hoja_sprites = pygame.image.load("fantasma.png").convert_alpha()
except FileNotFoundError:
    print("Error: No se encontró el archivo 'fantasma.png'")
    print("Por favor, descarga 'anim-nme-ghost.png' de OpenGameArt,")
    print("renómbralo a 'fantasma.png' y guárdalo en la carpeta.")
    pygame.quit()
    sys.exit()

# 5. Configuración de la animación
# --- ¡CAMBIOS IMPORTANTES AQUÍ! ---
FRAME_ANCHO = 32  # Esta imagen tiene frames de 32px de ancho
FRAME_ALTO = 32   # Y 32px de alto
NUM_FRAMES = 6    # ¡Esta animación tiene 6 frames!
INTERVALO_ANIMACION = 100 # en milisegundos

# --- TÉCNICA DEFINITIVA: "Copiar" los frames ---
frames_animacion = []
for i in range(NUM_FRAMES):
    area_frame = pygame.Rect(i * FRAME_ANCHO, 0, FRAME_ANCHO, FRAME_ALTO)
    frame = pygame.Surface((FRAME_ANCHO, FRAME_ALTO), pygame.SRCALPHA)
    frame.blit(hoja_sprites, (0, 0), area_frame)
    frames_animacion.append(frame)
# -----------------------------------------------

# 6. Variables de estado de la animación
frame_actual = 0
ultimo_update = pygame.time.get_ticks()

# 7. Reloj
reloj = pygame.time.Clock()

# Bucle principal del juego
ejecutando = True
while ejecutando:
    # 8. Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # --- Lógica de la Animación ---
    ahora = pygame.time.get_ticks()
    if ahora - ultimo_update > INTERVALO_ANIMACION:
        ultimo_update = ahora
        frame_actual = (frame_actual + 1) % NUM_FRAMES # (Se ajusta solo al 6)

    # 9. Dibujar
    pantalla.fill(FONDO_OSCURO) # Limpia la pantalla
    
    frame_para_dibujar = frames_animacion[frame_actual]
    
    # Lo escalamos (ej. x5)
    nuevo_ancho = FRAME_ANCHO * 5
    nuevo_alto = FRAME_ALTO * 5
    img_escalada = pygame.transform.scale(frame_para_dibujar, (nuevo_ancho, nuevo_alto))
    
    # Dibujar el frame escalado en el centro
    pos_x = (ANCHO - nuevo_ancho) // 2
    pos_y = (ALTO - nuevo_alto) // 2
    pantalla.blit(img_escalada, (pos_x, pos_y))


    # 10. Actualizar la pantalla
    pygame.display.flip()

    # 11. Limitar a 60 FPS
    reloj.tick(60)


# 12. Salir de Pygame
pygame.quit()
sys.exit()