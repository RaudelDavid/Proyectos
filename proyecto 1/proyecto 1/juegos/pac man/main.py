import pygame

# Inicializa Pygame
pygame.init()

# Define el tamaño de la ventana de pantalla
screen_width = 800
screen_height = 600

# Crea la ventana de pantalla
screen = pygame.display.set_mode((screen_width, screen_height))

# Establece el título de la ventana de pantalla
pygame.display.set_caption("Mi juego de Pygame")

# Define la posición y la velocidad inicial del personaje
x = 100
y = 100
vel = 0.5

# Carga la imagen del personaje
personaje_img = pygame.image.load('/home/raudel/Escritorio/code/juegos/pac man/img/pac man/pac1 abajo.png')

# Carga la imagen de fondo
fondo_img = pygame.image.load('/home/raudel/Escritorio/code/juegos/pac man/img/Arcade - Pac-Man - mapa lleno.jpg')

# Escala la imagen de fondo al tamaño de la pantalla
fondo_img = pygame.transform.scale(fondo_img, (screen_width, screen_height))


# Inicia el bucle principal del juego
running = True
while running:
    # Maneja los eventos de la ventana de pantalla y del teclado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screen_width - 50:
        x += vel
    if keys[pygame.K_UP] and y > 0:
        y -= vel
    if keys[pygame.K_DOWN] and y < screen_height - 50:
        y += vel

    # Renderiza los gráficos en la pantalla
    screen.blit(fondo_img, (0, 0))  # Renderiza el fondo en la pantalla
    screen.blit(personaje_img, (x, y))
    pygame.display.flip()

# Cierra Pygame
pygame.quit()


