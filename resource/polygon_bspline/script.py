import cairo
import pygame
import numpy as np
from resource.polygon_bspline import paint_bg
from resource.polygon_bspline import polygon

def no_1():
    # Setup Cairo surface dan context
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1000, 600)
    paint_bg.background(surface, color=[1, 1, 1])

    # Menggambar polygon dengan titik pusat (200, 200), radius 100, 6 sisi, dan sudut awal 30 derajat
    polygon.polygon(surface, titik_tengah=(200, 200), radius=100, sisi=6, sudut_mulai=30)

    # Simpan ke file
    surface.write_to_png("polygon.png")


def no_2():
    # Init Pygame
    pygame.init()

    WIDTH, HEIGHT = 1000, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Polygon Drawing Step by Step")

    # Menggunakan numpy untuk buffer antara Pycairo dan Pygame
    data = np.zeros((HEIGHT, WIDTH, 4), dtype=np.uint8)

    # Pycairo surface menggunakan numpy buffer
    surface = cairo.ImageSurface.create_for_data(data, cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    context = cairo.Context(surface)

    # Set background dengan Cairo
    paint_bg.background(surface, color=[1, 1, 1])

    # Parameter polygon
    titik_tengah = (200, 200)
    radius = 100
    sisi = 6
    sudut_mulai = 30
    langkah = 0  # Step awal untuk menggambar

    # Frame rate limiter
    clock = pygame.time.Clock()

    # Main loop Pygame
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return

        # Menggambar polygon satu langkah pada tiap loop
        if langkah <= sisi:
            langkah = polygon.polygon_step_by_step(context, titik_tengah, radius, sisi, sudut_mulai, langkah)

        # Konversi numpy buffer ke Pygame surface
        pygame_surface = pygame.image.frombuffer(data.tobytes(), (WIDTH, HEIGHT), "ARGB")

        # Tampilkan gambar di layar
        screen.blit(pygame_surface, (0, 0))
        pygame.display.flip()

        # Batasi kecepatan penggambaran
        clock.tick(100)  # Menggambar satu sisi per detik

# Fungsi utama untuk script
def script():
    no_2()

