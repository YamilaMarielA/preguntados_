# constantes.py

import pygame

# Constantes de colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Configuración de la ventana
VENTANA = (800, 600)

# Cargar imágenes
fondo = pygame.image.load("Segundo Parcial/fondoprincipal.jpg")
fondo = pygame.transform.scale(fondo, (800, 600))

imagen_boton = pygame.image.load("Segundo Parcial/botonpr.jpg")  # Imagen de botones
imagen_boton_hover = pygame.image.load("Segundo Parcial/botonhover.jpg")  # Imagen de botones cuando pasas el mouse
imagen_boton = pygame.transform.scale(imagen_boton, (200, 50))
imagen_boton_hover = pygame.transform.scale(imagen_boton_hover, (200, 50))

fondos_categoria = {
    'Historia': pygame.image.load("Segundo Parcial/HISTORIA.jpg"),
    'Matemática': pygame.image.load("Segundo Parcial/MATEMATICA.jpg"),
    'Entretenimiento': pygame.image.load("Segundo Parcial/ENTRETENIMIENTO.jpg"),
    'Deportes': pygame.image.load("Segundo Parcial/DEPORTES.jpg"),
    'Geografía': pygame.image.load("Segundo Parcial/geografiaa.jpg"),
}
